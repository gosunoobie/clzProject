from rest_framework import viewsets
from rest_framework.response import Response 
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from django.db.models import Sum, F
from .models import *
from .serializers import *
from .utils import get_weekday


class AirlineViewSet(viewsets.ModelViewSet):
    queryset = Airline.objects.all()
    serializer_class = AirlineSerializer

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class AirlineRouteViewSet(viewsets.ModelViewSet):
    queryset = AirlineRoute.objects.all()
    serializer_class = AirlineRouteSerializer

class SearchFlight(APIView):
    def get(self,request):

        return Response("this is the response")

    def post(self,request):
        serializer = SearchFlightSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        no_of_adults = serializer.validated_data.get("adult_passenger")
        no_of_child = serializer.validated_data.get("child_passenger")
        origin_city = serializer.validated_data.get("origin_location_code")
        destination_city = serializer.validated_data.get("destination_location_code")
        departure_date = request.data.get("departure_date") 
        weekday = get_weekday(departure_date)

        schedules = AirlineSchedule.objects.filter(
            airline_route__arrival__city_code__iexact=origin_city,
            airline_route__destination__city_code__iexact=destination_city,
            available_days__name= weekday
        )  
        avaiable_schedules = []
        for schedule in schedules:
            #booking = schedule.booking_set.all().aggregate(total_adult = Sum('no_of_adults'), total_child=Sum('no_of_child'))
            total_sum = schedule.booking_set.all().aggregate(total_sum = Sum(F('no_of_adults') + F('no_of_child')))
            print('total_sum ---------------------------', total_sum)
            total_sum = total_sum['total_sum'] or 0
            if total_sum + no_of_adults + no_of_child <= schedule.passenger_per_flight:
                avaiable_schedules.append(schedule)
        schedule_serializer = AirlineScheduleSerializer(avaiable_schedules, many=True, context={
            "no_of_adults": no_of_adults, 
            "no_of_child": no_of_child,
            "departure_code": origin_city,
            "arrival_code": destination_city
        })

        data = schedule_serializer.data
        for schedule in data:
            print(schedule, 'asdfsd')


        return Response(
            {
            "flightsCount": len(data),
            "flightsData" : data,
            }
                        )

class ReserveFlight(APIView):
    def post(self,request):
        flight_id = request.data.get("flight_id")
        return Response({
    "data": {
        "ReservationDetail": {
            "PNRDetail": [
                {
                    "AirlineID": "U4",
                    "FlightId": "4a8cbe18-790f-4b39-b4bc-979009ea165a",
                    "PNRNO": "EZL5ST",
                    "ReservationStatus": "OK",
                    "TTLDate": "26-Mar-2024",
                    "TTLTime": "600"
                }
            ],
            "ReserveTrackId": "f645e35b-13ec-4edc-a4ca-5208f8d7dbe2"
        }
    },
    "message": "Successfully returned data."
})

class ReserveFlightInfoTrackDetail(APIView):
    def get(self,request, guid):

        return Response({
    "data": {
        "flightInfo": [
            {
                "airline": "U4",
                "flightDate": "29-MAR-2024",
                "flightNo": "U4601",
                "departure": "KATHMANDU",
                "departureTime": "07:45",
                "arrival": "POKHARA",
                "arrivalTime": "08:10",
                "aircraftType": "BEECH",
                "adult": "1",
                "child": "0",
                "infant": "0",
                "flightId": "6f370101-8542-4965-b45c-79a43adecc2a",
                "flightClassCode": "Y",
                "currency": "NPR",
                "adultFare": "3470",
                "childFare": "2324.9",
                "infantFare": "347",
                "resFare": "6072.5",
                "fuelSurcharge": "2540",
                "tax": "500",
                "refundable": "T",
                "freeBaggage": "25",
                "agencyCommission": "200",
                "childCommission": "134",
                "duration": 598000,
                "arrivalCode": "PKR",
                "departureCode": "KTM",
                "airlineName": "BUDDHA AIRLINES",
                "airlineLogo": "http://usbooking.org/us/apiImages/U4.jpg",
                "totalPeople": 1,
                "totalCommissionedCost": 6310.0,
                "totalPrice": 6510,
                "discountAmount": 200.0,
                "rewardCoins": 631
            }
        ],
        "totalCost": 6310.0
    },
    "message": "Successfully returned data."
        })

class BookFlight(APIView):
    def post(self,request):
        serializer = BookingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data)

class BillingAddressViewSet(viewsets.ModelViewSet):
    serializer_class = BillingAddressSerializer
    queryset = BillingAddress.objects.all()

    def get_queryset(self):
        user = self.request.user
        print('user is -----------------------------', user)
        queryset = BillingAddress.objects.filter(user=user)
        return queryset

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)
