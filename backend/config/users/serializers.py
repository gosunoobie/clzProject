

from django.db.models import Q
from rest_framework import serializers, exceptions
from .models import *
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer as TokenObtainSerializer,
)

from .utils import get_pclaim
from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404
from django.db.transaction import atomic
from django.contrib.sites.shortcuts import get_current_site
from core.error_message import PHONE_NUMBER_TAKEN
from dj_rest_auth.serializers import JWTSerializer


class JWTCustomSerializer(JWTSerializer):
    """
    Serializer for JWT authentication. """

    access = serializers.CharField(source="access_token")
    refresh = serializers.CharField(source="refresh_token")
    user_detail = serializers.SerializerMethodField(method_name="get_user")

class UserSerializer(serializers.ModelSerializer):
    role = serializers.CharField(write_only=True)
    password_confirm = serializers.CharField(write_only=True)
    groups = serializers.SerializerMethodField()
    username = serializers.CharField(required=False)
    has_payment_detail = serializers.SerializerMethodField()

    class Meta:
        model = User
        exclude = (
            "phone_otp",
            "phone_time",
            "user_permissions",
            "is_staff",
            "reset_password_time",
            "reset_password_otp",
        )
        read_only_fields = (
            "date_joined",
            "last_login",
            "is_active",
            "is_superuser",
            "email_verified",
            "phone_verified",
            "is_deleted",
            "deleted_date",
            "total_reward_coin",
            "is_staff",
            "phone_otp",
            "phone_time",
            "reset_password_otp",
            "reset_password_time",
            
        )
        extra_kwargs = {
            "password": {"write_only": True, "min_length": 6},
        }


    def get_has_payment_detail(self, obj):
        return obj.has_added_payment_detail

    def get_groups(self, obj):
        return [group.name for group in obj.groups.all()]

    @atomic
    def create(self, validated_data):
        # print("---- created data ----")
        request = self.context.get("request")
        group_name = validated_data.pop("role", "")
        password = validated_data.pop("password", "")
        validated_data.pop("password_confirm", "")

        user = User(**validated_data)
        user.set_password(password)
        user.email_verified = True
        user.phone_verified = True
        user.is_active = True
        user.save()

        if group_name:
            group = get_object_or_404(Group, name=group_name)
            user.groups.add(group)

        site = get_current_site(request)
        # if user.nationality == "Nepal":
        #     user.generate_otp()

        # activate_user.delay(user.id, context)
        # full_name =
        user_details = {
            "user": user.get_full_name() if user.get_full_name() else user.username,
            "email": user.email,
            "groups": list(user.groups.values_list('name', flat=True)),
        }
        return user

    def update(self, instance, validated_data):
        """
        Don't allow email and mobile_number to be changed from this api
        """
        # if validated_data.get("mobile_number"):
        #     validated_data.pop("mobile_number")
        if validated_data.get("email"):
            validated_data.pop("email")
        return super().update(instance, validated_data)

    def validate(self, data):
        if self.context["request"].method == "POST":
            data["username"] = data["email"]
            if User.objects.filter(email=data.get("email")).exists():
                raise exceptions.ValidationError("User with this email already exists.")

            if data.get("password") != data.get("password_confirm"):
                raise exceptions.ValidationError("Passwords do not match")

            # if User.objects.filter(email=data["email"]).exists():
            #     raise exceptions.ValidationError("Email already taken")

            if User.objects.exclude(is_deleted=True).filter(mobile_number=data.get("mobile_number")).exists():
                print("what is worng")
                raise exceptions.ValidationError(PHONE_NUMBER_TAKEN )

        return super().validate(data)
    
    def to_representation(self, obj):
        response = super().to_representation(obj)
        request = self.context.get("request")
        response["messenger_url"]="http://m.me/cloudcruise"
        if request and obj.avatar:
            # print("inside here")
            response["avatar"] = request.build_absolute_uri(obj.avatar.url)
        return response

class EmptySerializer(serializers.Serializer):
    """
    Empty Seralizer that does not take or return any value
    """

    pass

class TokenObtainPairSerializer(TokenObtainSerializer):
    """
    Custom TokenObtainPairSerializer class that will add username to the token payload
    This can then be decoded by client to use the available data
    """

    DEVICE_CHOICES = (
        ("android", "android"),
        ("ios", "ios"),
        ("web", "web"),
    )
    fcm_token = serializers.CharField(max_length=500)
    fcm_type = serializers.ChoiceField(DEVICE_CHOICES)

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["username"] = user.username
        token["pclaim"] = get_pclaim(user)
        return token

    def validate(self, attrs):
        username = attrs.get("username")
        user = User.objects.filter(
            Q(username__iexact=username) | Q(mobile_number=username)
        ).first()
        refresh = self.get_token(user)
        data = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }
        return data
