from django.urls import path,include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()

router.register(r'airlines', AirlineViewSet, basename='airline')
router.register(r'city', CityViewSet, basename='city')
router.register(r'airline_route', AirlineRouteViewSet, basename='airline_route')
router.register('billing-address', BillingAddressViewSet, basename="billing-address")
router.register("khalti", KhaltiViewSet, basename="khalti_viewset")

urlpatterns = [
path('search-flights/', SearchFlight.as_view(), name="search"),
path('reserve/', ReserveFlight.as_view(), name="reserve"),
path('book-flights/', BookFlight.as_view(), name="book"),
path('passenger-info/', PassengerInfoView.as_view(), name="passengers"),
path('reserve-track/<str:guid>/', ReserveFlightInfoTrackDetail.as_view(), name="reserve_track_detail"),
path('txn-ticket-list/<str:txn_id>/', TransactionTicketList.as_view(), name="txn-ticket-list"),
path('download-ticket/<str:ticket_name>/<str:ticket_guid>.pdf', download_ticket, name="download-ticket"),
path('domestic-ticket-list/<int:booking_id>.pdf', download_domestic_ticket_list, name="download-ticket-list"),
path('', include(router.urls)),
]
