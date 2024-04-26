from rest_framework import viewsets
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response 
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from django.db.models import Sum, F
from rest_framework.decorators import action
from django.conf import settings
import requests
from core.utils import render_to_pdf
from django.db.transaction import atomic 
from django.http import HttpResponse
from .models import *
from .serializers import *
from .sector_list import (
    sectors,
    AIRLNAME_ID_NAME,
    AIRLNAME_TERMS_AND_CONDITIONS,
    SECTORS_KEY_VALUE,
    SECTORS_SHORT_CODE,
)
from .utils import get_weekday
import uuid


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
    @atomic
    def post(self,request):
        serializer = BookingSerializer(data=request.data)
        transaction = Transaction.objects.create(user=request.user, )
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        booking = Booking.objects.get(id=serializer.data.get('id'))
        schedule = booking.schedule
        total_cost = (booking.no_of_child or 0) * (schedule.child_fare or 0) + (booking.no_of_adults or 0) * (schedule.adult_fare or 0) 
        booking.transaction = transaction
        booking.save()
        transaction.total_amount = total_cost
        transaction.save()
        print(total_cost)

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

class PassengerInfoView(APIView):
    def post(self,request):
        data = request.data
        booking = get_object_or_404(Booking, id =data.get('booking_id')) 
        booking.contact_name = data.get("contact_name")
        booking.contact_email = data.get("contact_email")
        booking.contact_mobile = data.get("contact_mobile")
        booking.save()
        passengers=  data.get('passengers', [])
        print(passengers)
        for passenger in passengers :
            serializer = PassengerSerializer(data=passenger)
            if serializer.is_valid():
                serializer.save()

            else:
                return Response({
                    "message": serializer.errors 
                }, status=400)

        return Response({
            "message": 'Successfully added the passenger info',
                "data":{
                "booking_id": booking.id,
                "txn_id": booking.transaction.guid,
                "total_cost": booking.transaction.total_amount,
            }  ,

        })
    
    def get(self,request):
        passenger = PassengerInfo.objects.first()
        serializer = PassengerSerializer(passenger)
        return Response({
            "data": serializer.data
        })








class KhaltiViewSet(GenericViewSet):
    """
     Visit https://docs.khalti.com/khalti-epayment/ for more detail
     Flow for Khalti Payment:

     1) Initiate Payment API needs to called first (in this case 'inititiate_payment' action does that)
     2) You need to provide website url and return url where khalti redirects after success payment
     3) as success initiation, khalti provides "payment_url" and we redirect to that payment_url
     4) After success payment, call verify_payment to validate payment and update transaction and generate tickets

    """

    khalti_key = settings.EPAY_KHALTI_SECRET


    def initiate_khalti_payment(self,payload):
        url = f"{settings.EPAY_KHALTI_URL}/api/v2/epayment/initiate/"
        headers = {"Authorization": f"Key {self.khalti_key}"}
        print("This is the payload",payload)
        print('url is ',url)
        response = requests.request("POST", url, headers=headers, data=payload)
        print("This is the response from khalti:",response)
        return response

    @action(detail=False, methods=['post'])
    def inititiate_payment(self, request):
        """
        Initial Api for khalti epayment
        This gives khalt's payment url where we should be redirected to
        """
        try:
            txn_id = request.data.get("txn_id")
            txn = get_object_or_404(Transaction,guid=txn_id)

            payload = {
                    "return_url": f"{settings.KHALTI_WEB_RETURN_DOMAIN}/payment-success/khalti/",
                    "website_url": settings.KHALTI_WEB_RETURN_DOMAIN,
                    "amount": 1000,
                    "purchase_order_id":txn_id,
                    "purchase_order_name": "test",
            
            }
            response = self.initiate_khalti_payment(payload)
            print("This is the response againL",response.text)
            #creating khaltiresponse track
            #end
            if response.status_code != 200:
                raise exceptions.APIException("Khalti Payment Initiaiton Failed")
            json_response = response.json()
            print("json response of web callback",json_response)
            
            return Response(json_response)
        except Exception as e:
            print("----- Khalti initiate error ---- ", e)
            raise exceptions.APIException(str(e))
        

    @action(detail=False, methods=['post'])
    def verify_payment(self, request):
        """
        After khalti payment is successfull, it redirects us to url we provide during initiate payment api
        In that page, call this api to verify payment and update transaction if valid
        """
        #serializer = KhaltiWebVerifySerializer(data=request.data)
        #serializer.is_valid(raise_exception=True)
        url = f"{settings.EPAY_KHALTI_URL}/api/v2/epayment/lookup/"
        headers = {"Authorization": f"Key {self.khalti_key}"}
        data = request.data
        #print("This is the request.data in khalti verification in web version:",data)
        txn = get_object_or_404(Transaction,guid=data.get("txn_id"))
        response = requests.request("POST", url, headers=headers, data={"pidx":data.get("pidx")})
        # print(response.text)
        #khalti_response_track = get_object_or_404(KhaltiCallbackResponseTrack, product_id=txn.txn_id)
        #khalti_response_track.reference_id = data.get("pidx")
        #khalti_response_track.verification_request_payload = data.get("pidx")
        #khalti_response_track.verification_response = response.json()
        #khalti_response_track.save()
        if response.status_code != 200:
            raise exceptions.APIException("ERROR CAME")

        json_response = response.json()
        print("This is the response we get after verification in khalti in web:",json_response)
        if txn.status != "Completed":
            txn.payment_method_name = "Khalti"
            txn.payment_method = "Wallet"
            txn.status = "Paid"
            txn.currency = "NPR"
            txn.paid_amount = json_response["total_amount"]/100 #convert to rupees
            txn.payment_providers_txn_id =json_response["transaction_id"]
            txn.save()

        if txn.status == "Paid":
            # update domestic flights related
            # up_flights =  IssueFlightTicketService()
            #up_flights.issue_ticket(request,txn)
            booking = txn.booking_set.first()
            passengers = booking.passengerinfo_set.all()
            for passenger in passengers:
                ticket, created = FlightTicket.objects.get_or_create(

                    user = request.user,
                    first_name = passenger.first_name,
                    last_name = passenger.last_name,
                    issued_date = passenger.booking.for_date,
                    arrival_destination = passenger.booking.schedule.airline_route.destination,
                    departure_destination = passenger.booking.schedule.airline_route.arrival,
                    arrival_time = passenger.booking.schedule.arrival_time,
                    booking = booking,
                    airline_code = passenger.booking.schedule.airline_route.airline.code,
                    flight_no= passenger.booking.schedule.flight_id,
                    pnr_no = str(uuid.uuid4())
                )

            txn.status = "Completed"
            txn.save()
               # ticket = FlightTicket(
               #     user = request.user,
               #     first_name = passenger.first_name,
               #     last_name = passenger.last_name,
               #     issued_date = passenger.booking.for_date,
               #     arrival_destination = passenger.booking.schedule.airline_route.destination,
               #     departure_destination = passenger.booking.schedule.airline_route.arrival,
               #     arrival_time = passenger.booking.schedule.arrival_time,
               #     booking = booking,
               #     pnr_no = str(uuid.uuid4())
               # ) 
               # ticket.save()
            generate_domestic_ticket_list(booking.id)
            

        txn_serializer=TransactionSerializer(txn,context={"request":request})
        return Response(txn_serializer.data)


def generate_domestic_ticket_list(booking_id):
    booking=Booking.objects.get(id=booking_id)
    booking_tickets = booking.flightticket_set.all()

    data={
        "booking":booking,
        "booking_tickets":booking_tickets
    }
    pdf = render_to_pdf("domestic_tickets_list_pdf.html", data)
    return pdf

class TransactionTicketList(APIView):
    serializer_class = FlightTicketSerializer

    def get(self,request,txn_id):
        print('txn_id-------------------------',txn_id)
        
        txn = get_object_or_404(Transaction,guid=txn_id)
        if txn.user != request.user:
            raise exceptions.ValidationError("You are not authorized to view this.")
        


        domestic_flight_tickets = FlightTicket.objects.filter(booking__transaction=txn)
        dom_serializer = FlightTicketSerializer(domestic_flight_tickets,many=True,context={"request":request})

        
        return Response({"domestic_tickets":dom_serializer.data})

def download_ticket(request, ticket_name, ticket_guid):
    
    ticket = get_object_or_404(FlightTicket, guid=ticket_guid)
    
    #total_fare = ticket.total_commissioned_cost
    #tax = ticket.tax_amount

    airline_name = AIRLNAME_ID_NAME.get(ticket.airline_code, ticket.airline_code)
    departure_destination = SECTORS_KEY_VALUE.get(
        ticket.departure_destination, ticket.departure_destination
    )
    arrival_destination = SECTORS_KEY_VALUE.get(
        ticket.arrival_destination, ticket.arrival_destination
    )

    airline_name = AIRLNAME_ID_NAME.get(ticket.airline_code, ticket.airline_code)

    data = {
        "ticket": ticket,
        "payment_method": "E-SEWA",
        "domain": request.META["HTTP_HOST"],
        "airline_name": airline_name,
        "departure_destination": departure_destination,
        "arrival_destination": arrival_destination,

    }
    pdf = render_to_pdf("ticket.html", data)
    return HttpResponse(pdf, content_type="application/pdf")


def download_domestic_ticket_list(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    booking_tickets = booking.flightticket_set.all()

    data = {"booking": booking, "booking_tickets": booking_tickets}
    pdf = render_to_pdf("domestic_tickets_list_pdf.html", data)
    return HttpResponse(pdf, content_type="application/pdf")
