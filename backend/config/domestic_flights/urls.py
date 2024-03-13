from django.urls import path,include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()

router.register(r'airlines', AirlineViewSet, basename='airline')
router.register(r'city', CityViewSet, basename='city')
router.register(r'airline_route', AirlineRouteViewSet, basename='airline_route')
router.register('billing-address', BillingAddressViewSet, basename="billing-address")

urlpatterns = [
path('search-flights/', SearchFlight.as_view(), name="search"),
path('reserve/', ReserveFlight.as_view(), name="reserve"),
path('book-flights/', BookFlight.as_view(), name="book"),
    path('reserve-track/<str:guid>/', ReserveFlightInfoTrackDetail.as_view(), name="reserve_track_detail"),
path('', include(router.urls)),
]
