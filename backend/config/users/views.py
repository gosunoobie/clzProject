import jwt
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, permissions, status
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken
from rest_framework.decorators import action
from rest_framework.exceptions import APIException, ValidationError
from .permissions import UserObjPermission, IsTheUserPermission
from rest_framework.status import HTTP_401_UNAUTHORIZED
from django.conf import settings
from rest_framework import exceptions
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.utils import aware_utcnow, datetime_from_epoch
from .utils import refresh_cookie, get_pclaim, create_fcm_device
from django.db.models import Q
from rest_framework import (
    viewsets,
    permissions,
    status,
)
from core.pagination import CustomPageNumberPagination

from .serializers import EmptySerializer, TokenObtainPairSerializer
from django.shortcuts import get_object_or_404
from .models import *
from users.serializers import UserSerializer
from core.error_message import *
from core.success_message import *

class UsersCreate(APIView):
    def get(self, request, format=None):
        return Response('this is the user creation')

class TokenObtainPairViewSet(GenericViewSet, TokenObtainPairView):
    """
    Custom TokenObtainPairViewSet class that will send refresh token as an http only cookie.
    """

    permission_classes = [permissions.AllowAny]
    serializer_class = TokenObtainPairSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["request"] = self.request
        return context

    def create(self, request, *args, **kwargs):
        """
        API that will return access and refresh token. It will also return refresh token as an http only cookie.
        """
        # print("------------------creating token------------------")
        # print(request.data)
        # lower_username = request.data.get("username").lower()
        # print("this is lower=",lower_username)
        user = User.objects.filter(
            Q(username__iexact=request.data.get("username"))
            | Q(mobile_number=request.data.get("username"))
        ).first()

        # if not user or not user.check_password(request.data.get("password")):
        #     raise ValidationError(USER_NOT_FOUND)
        if not user:
            raise ValidationError(INCORRECT_EMAIL)
        elif user and not user.check_password(request.data.get("password")):
            raise ValidationError(INCORRECT_PASSWORD)
       
        if not user.phone_verified and user.nationality == "Nepal":
            user.generate_otp()
            # return Response(
            #     {
            #         "user": UserSerializer(user).data,
            #         "message": VERIFY_PHONE_NUMBER,
            #     }
            # )
        response = super().post(request=request, *args, **kwargs)
        response = refresh_cookie(response)
        jwt_decoded = jwt.decode(response.data["access"], settings.SECRET_KEY, "HS256")
        user = get_object_or_404(User, id=jwt_decoded.get("user_id"))
        response.data["user"] = UserSerializer(user, context={"request": request}).data

        fcm_data = {
            "user_id": user.id,
            "fcm_type": request.data.get("fcm_type"),
            "fcm_token": request.data.get("fcm_token"),
        }

        create_fcm_device(fcm_data)
        return response


class TokenRefreshViewSet(GenericViewSet, TokenRefreshView):
    """
    Custom TokenRefreshViewSet class that takes refresh token from cookies when refresh is not present in post data.
    It also returns refresh token if ROTATE_REFRESH_TOKENS is true and it gets 'refresh' in response's data.
    """

    permission_classes = [permissions.AllowAny]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["request"] = self.request
        return context

    def create(self, request, *args, **kwargs):
        """
        API that refreshes access token. This API will try to take refresh token from cookies when refresh is not present in post data.
        """

        key_name = "pclaim"
        if not "refresh" in request.COOKIES.keys():
            response = Response(
                {"message": "No Refresh Token"},
                status=HTTP_401_UNAUTHORIZED,
            )
            response.delete_cookie("refresh")
            return response
        request.data["refresh"] = request.COOKIES["refresh"]
        try:
            response = super().post(request=request, *args, **kwargs)
            jwt_decoded = jwt.decode(
                response.data["access"], settings.SECRET_KEY, "HS256"
            )
            user = get_user_model().objects.get(id=jwt_decoded["user_id"])
            response.data["user"] = UserSerializer(
                user, context={"request": request}
            ).data
            return response
        except Exception as e:
            response = Response(
                {"message": "Token not valid."}, status=HTTP_401_UNAUTHORIZED
            )
            response.delete_cookie("refresh")
            return response


class ClearTokenViewSet(GenericViewSet):
    """
    Create ViewSet to clear refresh token in client.
    """

    permission_classes = [permissions.AllowAny]
    serializer_class = EmptySerializer

    def create(self, request, *args, **kwargs):
        """
        API that will clear the http only refresh token for client.
        """
        OutstandingToken.objects.filter(expires_at__lte=aware_utcnow()).delete()
        # print("cookies are ",request.COOKIES)
        if "refresh" in request.COOKIES:
            refresh = request.COOKIES["refresh"]
            print("refres is ",refresh)
            try:
                jwt_decoded = jwt.decode(refresh, settings.SECRET_KEY, "HS256")
                print("this is jwt-decoded=",jwt_decoded)
                if (
                    "jti" in jwt_decoded
                    and "exp" in jwt_decoded
                    and "user_id" in jwt_decoded
                ):
                    jti = jwt_decoded["jti"]
                    exp = jwt_decoded["exp"]
                    user_id = jwt_decoded["user_id"]
                    token = OutstandingToken.objects.filter(
                        jti=jti,
                        user_id=user_id,
                        expires_at=datetime_from_epoch(exp),
                    )
                    token.delete()
            except:
                print("Error")
                pass

        response = Response()
        response.delete_cookie("refresh", domain=settings.HTTP_ONLY_COOKIE_DOMAIN)
        response.delete_cookie("jwt-auth", domain=settings.HTTP_ONLY_COOKIE_DOMAIN)
        response.delete_cookie("sessionid")
        # response.set_cookie("refresh", domain=settings.HTTP_ONLY_COOKIE_DOMAIN, httponly=True, samesite="Lax")
        response.status_code = 204  
        return response


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny, UserObjPermission]
    pagination_class = CustomPageNumberPagination
    pagination_class.page_size = 10

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["request"] = self.request
        return context

    @action(["patch", "put"], detail=False, permission_classes=[IsTheUserPermission])
    def update_info(self, request, *args, **kwargs):
        try:
            partial = True
            instance = self.request.user
            serializer = self.get_serializer(
                instance, data=request.data, partial=partial
            )
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            if getattr(instance, "_prefetched_objects_cache", None):
                instance._prefetched_objects_cache = {}
            return Response(serializer.data)
        except Exception as e:
            raise ValidationError(str(e))

    """ @action(["post"], detail=False, permission_classes=[IsTheUserPermission])
    def change_password(self, request, *args, **kwargs):
        try:
            user = request.user
            serializer = PasswordChangeSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(user=user)
            return Response({"message": SUCCESSFUL_PASSWORD_CHANGE})
        except Exception as e:
            raise APIException(e)

    @action(["post"], detail=True)
    def send_otp(self, request, *args, **kwargs):
        try:
            data = self.get_object().generate_otp()
            return Response(data)
        except Exception as e:
            raise ValidationError(str(e))
"""
    @action(["get"], detail=False)
    def my_info(self, request, *args, **kwargs):
        instance = self.request.user
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @action(["get"], detail=False)
    def get_total_reward_coin(self, request, *args, **kwargs):
        from django.db.models import Sum

        try:
            user = self.request.user
            active_coin = user.loyaltycointransaction_set.filter(status="ACTIVE").aggregate(active_coin=Sum("coin_amount"))["active_coin"] or 0
            inactive_coin = user.loyaltycointransaction_set.exclude(status="ACTIVE").aggregate(inactive_coin=Sum("coin_amount"))["inactive_coin"] or 0
            total_coin = active_coin - inactive_coin
            # total_coin = user.total_reward_coin or 0.0
            tier_point = total_coin / 100
            if tier_point < 500:
                status = "Bronze"
                next_tier_level = "Silver"
                l_limit = 0
                u_limit = 500
            elif tier_point < 1000:
                status = "Silver"
                next_tier_level = "Gold"
                l_limit = 500
                u_limit = 1000
            elif tier_point < 1500:
                status = "Gold"
                next_tier_level = "Platinum"
                l_limit = 1000
                u_limit = 1500
            else:
                status = "Platinum"
                next_tier_level = "Platinum"
                l_limit = 1500
                u_limit = None

            return Response(
                {
                    "total_reward_coin": total_coin,
                    "tier_point": tier_point,
                    "status": status,
                    "l_limit": l_limit,
                    "u_limit": u_limit,
                    "tier_level": f"{tier_point} out of {u_limit}"
                    if u_limit
                    else f"{tier_point} tier point",
                    "next_tier_level": next_tier_level,
                }
            )
        except Exception as e:
            raise ValidationError(str(e))

    @action(["post"], detail=False)
    def update_number(self, request, *args, **kwargs):
        try:
            user = request.user
            number = request.data.get("mobile_number")
            country = request.data.get("country")
            if not number and country == "Nepal":
                return Response(
                    {"message": MOBILE_NO_BLANK},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            # if (
            #     User.objects.exclude(Q(id=user.id) | Q(is_deleted=True)).id
            #     .filter(mobile_number=number)
            #     .exists()
            # ):
            #     return Response(
            #         {"message": PHONE_NUMBER_TAKEN},
            #         status=status.HTTP_400_BAD_REQUEST,
            #     )
            query = Q(mobile_number__isnull=False) & ~Q(mobile_number__exact='')
            print(type(user.id))
            if User.objects.exclude(is_deleted=True).exclude(id=user.id).filter(query, mobile_number=number).exists():
                print("what is wrong")
                raise exceptions.ValidationError(PHONE_NUMBER_TAKEN)
            if number:
                user.mobile_number = number
            user.phone_verified = False
            user.nationality = country
            user.save()
            if country == "Nepal":
                user.generate_otp()
            return Response({"message": SUCCESSFUL_MOBILE_NO_UPDATE})
        except Exception as e:
            # raise ValidationError(str(e))
            raise ValidationError(PHONE_NUMBER_TAKEN)
    
    @action(["post"], detail=False)
    def add_number(self, request, *args, **kwargs):
        try:
            user_id = request.data.get("user_id")
            number = request.data.get("mobile_number")
            country = request.data.get("country")
            user_obj = get_object_or_404(User, id=user_id)
            if not number and country == "Nepal":
                return Response(
                    {"message": MOBILE_NO_BLANK},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            if number:
                user_obj.mobile_number = number
            user_obj.phone_verified = False
            user_obj.nationality = country
            user_obj.save()
            if country == "Nepal":
                user_obj.generate_otp()
            return Response({"message": SUCCESSFUL_MOBILE_NO_ADD})
        except Exception as e:
            raise ValidationError(str(e))

    @action(["post"], detail=True)
    def verify_otp(self, request, *args, **kwargs):
        data = self.get_object().verify_otp(request.data.get("otp"))
        if data.get("success") == True:
            if data.get("success") != None:
                data.pop("success")
            return Response(data, status=status.HTTP_200_OK)
        else:
            if data.get("success") != None:
                data.pop("success")
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        

    @action(["post"], detail=True)
    def generate_email_otp(self, request, *args, **kwargs):
        try:
            data = self.get_object().generate_email_otp()
            return Response(data)
        except Exception as e:
            raise ValidationError(str(e))

    """ @action(["post"], detail=True)
    def verify_email_otp(self, request, *args, **kwargs):
        email_otp = request.data.get("otp")
        user = self.get_object()
        print("user is ",user)
        try:
            if user.email_verified:
                return Response({"message": "Your email is already verified."})
            if user.email_otp != email_otp:
                raise APIException("OTP is incorrect.")
            user.email_verified = True
            user.is_active = True
            user.save()
            send_email_verified_email.delay(
                user.email, user.get_full_name() or user.username
            )
            return Response({"message": "Successfully verified email address."})
        except Exception as e:
            raise APIException(str(e)) """
        

    @action(["post"], detail=False, permission_classes=[IsTheUserPermission])
    def delete_my_account(self, request, *args, **kwargs):
        try:
            user = request.user
            if user.is_deleted == True:
                raise APIException("Your account is already deleted!")
            if user.account_provider != "CloudCruise":
                user.soft_delete()
                return Response({"message": "Account succesfully deleted."})
            password = request.data.get("password")
            if not user.check_password(password):
                raise APIException(INCORRECT_PASSWORD)
            user.soft_delete()
            return Response({"message": "Account succesfully deleted."})

        except Exception as e:
            raise ValidationError(str(e))

    """ @action(["post"], detail=True, permission_classes=[IsTheUserPermission])
    def add_update_payment_detail(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = VPaymentDetailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            serializer.save(user=user)
            return Response({"message": SUCCESSFUL_PAYMENT_INFO_UPDATE})
        except Exception as e:
            raise ValidationError(
                "DB Constraint Failed. Ensure that User has unique priority and account id."
            )
"""


        
    @action(["post"], detail=False)
    def add_name(self, request, *args, **kwargs):
        try:
            user_id = request.data.get("user_id")
            first_name = request.data.get("first_name")
            last_name = request.data.get("last_name")
            user_obj = get_object_or_404(User, id=user_id)
            if not first_name or not last_name:
                return Response(
                    {"message": "Please add both of your first and last name."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            user_obj.first_name = first_name
            user_obj.last_name = last_name
            user_obj.save()
            return Response({"message": "Detail successfully added."})
        except Exception as e:
            raise ValidationError(str(e))
