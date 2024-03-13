import jwt
from rest_framework_simplejwt.token_blacklist.models import (
    BlacklistedToken,
    OutstandingToken,
)
from django.conf import settings
from users.models import User
from django.shortcuts import get_object_or_404
from fcm_django.models import FCMDevice


def refresh_cookie(response):
    # print(response.data["access"])
    args = ["refresh", response.data["refresh"]]
    response.set_cookie(*args,domain=settings.HTTP_ONLY_COOKIE_DOMAIN,httponly=True)
    return response


def blacklist_refresh_token(user):
    for token in OutstandingToken.objects.filter(user=user).exclude(
        id__in=BlacklistedToken.objects.filter(token__user=user).values_list(
            "token_id", flat=True
        ),
    ):
        BlacklistedToken.objects.create(token=token)


def get_pclaim(user):
    try:
        claim = user.password[-10:]
        bclaim = claim.encode("utf-8")
        pclaim = str(int.from_bytes(bclaim, "big"))
        return pclaim
    except Exception as e:
        print(e)
        return None


def create_fcm_device(data):
    user_id = data.get("user_id")
    user = User.objects.filter(id=user_id).first()
    FCMDevice.objects.update_or_create(
        registration_id=data.get("fcm_token"),
        defaults={
            "registration_id": data.get("fcm_token"),
            "user": user,
            "type": data.get("fcm_type"),
        },
    )
