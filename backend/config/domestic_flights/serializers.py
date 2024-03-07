
from rest_framework import serializers
from datetime import datetime, date
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

class AirlineScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirlineSchedule
        fields = '__all__'

class SearchFlightSerializer(serializers.Serializer):
    departure_date = serializers.DateField()
    destination_location_code = serializers.CharField(max_length=3)
    origin_location_code = serializers.CharField(max_length=3)
    return_date = serializers.DateField(required=False)
    nationality = serializers.CharField(max_length=2)
    adult_passenger = serializers.IntegerField(required=True)
    child_passenger = serializers.IntegerField(default=0)
    return_flight = serializers.BooleanField(default=False)



    def validate(self, value):
        maximum_passenger_limit = 9
        today_date = date.today()
        if value.get("departure_date") < today_date:
            raise serializers.ValidationError(
                "Departure date should be today or in the future"
            )

        if (
            value.get("destination_location_code")
            and not value.get("destination_location_code").isupper()
        ):
            raise serializers.ValidationError(
                "Destination Location must be in capital LETTERS and should not be integer."
            )

        if (
            value.get("origin_location_code")
            and not value.get("origin_location_code").isupper()
        ):
            raise serializers.ValidationError(
                "Origin Location must be in capital LETTERS and should not be integer."
            )

        if (
            value.get("adult_passenger") + value.get("child_passenger")
            > maximum_passenger_limit
        ):
            raise serializers.ValidationError(
                f"No of passengers cant exceed {maximum_passenger_limit}"
            )

        return value

class BookingSerializer(serializers.Serializer):
    booking_id = serializers.IntegerField(required=True)
    no_of_adults = serializers.IntegerField(required=True)
    no_of_children = serializers.IntegerField(default=0)
    no_of_infant = serializers.IntegerField(default=0)
