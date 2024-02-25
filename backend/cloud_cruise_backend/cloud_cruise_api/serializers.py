from rest_framework import serializers
from .models import *

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class AirlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airline
        fields = '__all__'

class AirlineRouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirlineRoute
        fields = '__all__'
