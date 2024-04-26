from rest_framework import serializers
from datetime import datetime, date
from .models import *
from rest_framework import viewsets, exceptions

from .sector_list import (
    sectors,
    AIRLNAME_ID_NAME,
    AIRLNAME_TERMS_AND_CONDITIONS,
    SECTORS_KEY_VALUE,
    SECTORS_SHORT_CODE,
)


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"


class AirlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airline
        fields = "__all__"


class AirlineRouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirlineRoute
        fields = "__all__"


class AirlineScheduleSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()
    departure_code = serializers.SerializerMethodField()
    arrival_code = serializers.SerializerMethodField()
    total_commissioned_cost = serializers.SerializerMethodField()
    airline_name = serializers.SerializerMethodField()
    airline = serializers.SerializerMethodField()
    arrival = serializers.SerializerMethodField()
    departure = serializers.SerializerMethodField()
    currency = serializers.SerializerMethodField()
    no_of_adults = serializers.SerializerMethodField()
    no_of_child = serializers.SerializerMethodField()

    class Meta:
        model = AirlineSchedule
        fields = "__all__"

    def get_no_of_adults(self, obj):
        no_of_adults = self.context.get("no_of_adults", 0)
        return no_of_adults

    def get_no_of_child(self, obj):
        no_of_child = self.context.get("no_of_child", 0)
        return no_of_child

    def get_total_price(self, obj):
        no_of_adults = self.context.get("no_of_adults", 0)
        no_of_child = self.context.get("no_of_child", 0)

        return obj.adult_fare * no_of_adults + obj.child_fare * no_of_child

    def get_departure_code(self, obj):
        origin_city = self.context.get("departure_code")
        return origin_city

    def get_arrival_code(self, obj):
        destination_city = self.context.get("arrival_code")
        return destination_city

    def get_total_commissioned_cost(self, obj):

        no_of_adults = self.context.get("no_of_adults", 0)
        no_of_child = self.context.get("no_of_child", 0)

        total_price = obj.adult_fare * no_of_adults + obj.child_fare * no_of_child
        return total_price - obj.discount_amount

    def get_airline_name(self, obj):
        return obj.airline_route.airline.name

    def get_airline(self, obj):
        if obj.airline_route.airline.logo:
            return f"http://127.0.0.1:8000/{obj.airline_route.airline.logo.url}"
        else:
            return None

    def get_arrival(self, obj):
        return obj.airline_route.arrival.city_name

    def get_departure(self, obj):
        return obj.airline_route.destination.city_name

    def get_currency(self, obj):
        return "NPR"


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
            value.get("adult_passenger", 0) + value.get("child_passenger", 0)
            > maximum_passenger_limit
        ):
            raise serializers.ValidationError(
                f"No of passengers cant exceed {maximum_passenger_limit}"
            )

        return value


class BookingSerializer(serializers.ModelSerializer):
    schedule_detail = serializers.SerializerMethodField()

    class Meta:
        model = Booking
        read_only_fields = ["user"]
        fields = "__all__"

    def get_schedule_detail(self, obj):
        return [
            AirlineScheduleSerializer(
                obj.schedule,
                context={
                    "no_of_adults": obj.no_of_adults,
                    "no_of_child": obj.no_of_child,
                },
            ).data
        ]


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PassengerInfo
        fields = "__all__"


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"


class BillingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillingAddress
        exclude = ("user",)


class KhaltiRequestSerializer(serializers.Serializer):
    token = serializers.CharField()
    amount = serializers.IntegerField()
    txn_id = serializers.CharField()


class EsewaWebRequestSerializer(serializers.Serializer):
    amt = serializers.IntegerField()
    rid = serializers.CharField()
    pid = serializers.CharField()
    scd = serializers.CharField()


class KhaltiWebVerifySerializer(serializers.Serializer):
    txn_id = serializers.CharField()
    pidx = serializers.CharField()


class FlightTicketSerializer(serializers.ModelSerializer):
    ticket_url = serializers.SerializerMethodField()

    class Meta:
        model = FlightTicket
        fields = "__all__"

    def get_ticket_url(self, obj):
        request = self.context.get("request")
        domain = f"{request.scheme}://{request.META['HTTP_HOST']}"
        ticket_guid = obj.guid
        airline = obj.airline_code
        print("air line name is ", airline)
        print("airline id name is ", AIRLNAME_ID_NAME)
        airline_name = AIRLNAME_ID_NAME.get(airline, "-")
        flight_no = obj.flight_no
        ticket_no = obj.id
        ticket_name = f"CloudCruise__{airline_name}__{airline}{flight_no}__{ticket_no}"
        # ticket = f"{domain}/domestic/download-ticket/{ticket_no}.pdf"
        ticket = f"{domain}/api/download-ticket/{ticket_name}/{ticket_guid}.pdf"
        return ticket


class CustomTimeField(serializers.TimeField):
    def to_representation(self, value):
        # Override the to_representation method to format time as "hh:mm"
        return value.strftime("%H:%M")
