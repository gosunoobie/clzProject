
from django.urls import path,include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()

router.register(r'airlines', AirlineViewSet, basename='airline')
router.register(r'city', CityViewSet, basename='city')
router.register(r'airline_route', AirlineRouteViewSet, basename='airline_route')

urlpatterns = [
path('', include(router.urls)),
]
