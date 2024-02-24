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
        serializer = SearchFlightSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        origin_city = request.data.get("origin_location_code")
        destination_city = request.data.get("destination_location_code")
        schedules = AirlineSchedule.objects.filter(airline_route__arrival__city_code=origin_city, airline_route__destination__city_code=destination_city)
        schedule_serializer = AirlineScheduleSerializer(schedules, many=True)

        print(schedules)
        return Response(schedule_serializer.data)

