from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import (
    TokenObtainPairViewSet,
    TokenRefreshViewSet,
    ClearTokenViewSet,
    UserViewSet,
)
from fcm_django.api.rest_framework import FCMDeviceAuthorizedViewSet


router = SimpleRouter()

router.register("auth", UserViewSet, basename="user")
router.register("jwt", TokenObtainPairViewSet, basename="jwt")
router.register("jwt/refresh", TokenRefreshViewSet, basename="jwt_refresh")
router.register("jwt/clear", ClearTokenViewSet, basename="jwt_clear")

# firebase urls
router.register("fcm/devices", FCMDeviceAuthorizedViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
