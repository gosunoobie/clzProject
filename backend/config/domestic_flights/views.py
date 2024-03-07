from rest_framework import viewsets
from rest_framework.response import Response 
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from .models import *
from .serializers import *


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
        no_of_adults = request.data.get("adult_passenger")
        no_of_children = request.data.get("child_passanger")
        origin_city = request.data.get("origin_location_code")
        destination_city = request.data.get("destination_location_code")
        serializer = SearchFlightSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        schedules = AirlineSchedule.objects.filter(airline_route__arrival__city_code__iexact=origin_city, airline_route__destination__city_code__iexact=destination_city)
        schedule_serializer = AirlineScheduleSerializer(schedules, many=True)
        data = schedule_serializer.data
        for schedule in data:
            print(schedule, 'asdfsd')


        return Response(
            {
            "flightsCount": len(data),
            "flightsData" : data,
            }
                        )

class BookFlight(APIView):
    def post(self,request):
        booking_id = request.data.get("id")
        no_of_passengers = request.data.get("no_of_adults") + request.data.get("no_of_children") + request.data.get("no_of_infant")
        serializer = BookingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        schedule = AirlineSchedule.objects.filter(id=booking_id)
        print(schedule) 
        if schedule.get_is_seat_available():
           schedule.passenger_per_flight = schedule.passenger_per_flight - no_of_passengers 


        return Response(serializer.data)
