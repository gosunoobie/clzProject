from django.db import models
from multiselectfield import MultiSelectField
from core.models import SoftDeleteModel, TimeStampedModel, SingletonModel
import uuid
from users.models import User


class Airline(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='airline/', null=True, blank=True)

    def __str__(self):
        return self.name

class City(models.Model):
    city_name = models.CharField(max_length=50, unique=True)
    city_code = models.CharField(max_length=3, unique=True)

    def __str__(self):
        return self.city_name

class AirlineRoute(models.Model):
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE )
    arrival = models.ForeignKey(City, on_delete=models.CASCADE, related_name="arrival_route" )
    destination = models.ForeignKey(City, on_delete=models.CASCADE, related_name="destination_route")
    flights_per_day = models.IntegerField()
    aircraft_type = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.airline.name}({self.arrival.city_name} - {self.destination.city_name})" 

class WeekDays(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Week days'


class AirlineSchedule(models.Model):

    airline_route = models.ForeignKey(AirlineRoute, on_delete=models.CASCADE )
    passenger_per_flight = models.IntegerField()
    adult_fare = models.IntegerField()
    child_fare = models.IntegerField()
    departure_time = models.TimeField()
    arrival_time = models.TimeField()
    refundable = models.BooleanField(default=False)
    free_baggage = models.IntegerField()
    elapsed_time = models.IntegerField()
    discount_amount = models.IntegerField()
    flight_class_code = models.CharField(max_length=10, null=True, blank=True)
    available_days = models.ManyToManyField(WeekDays)
    flight_id = models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return f"{self.airline_route}{self.departure_time}-{self.arrival_time}"

    @property
    def get_is_seat_available(self):
        if self.passenger_per_flight < 1:
            return False
        else:
            return True

    def get_available_days_list(self):
        return self.available_days.split(",")




class Booking(models.Model):

    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Pending', 'Pending'),
        ('Cancelled', 'Cancelled'),
    ]
    created_date = models.DateTimeField(auto_now_add=True, null=True) 
    user = models.ForeignKey("users.User",on_delete=models.CASCADE)
    schedule = models.ForeignKey(AirlineSchedule,on_delete=models.CASCADE)
    no_of_adults = models.IntegerField()
    no_of_child = models.IntegerField()
    status = models.CharField(max_length=10,choices=STATUS_CHOICES, default="Pending" )
    transaction = models.ForeignKey("domestic_flights.transaction",on_delete=models.CASCADE,null=True)

    @property
    def get_total_passengers(self):
        return self.no_of_adults + self.no_of_child




class BillingAddress(TimeStampedModel):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    pan_or_vat_num = models.IntegerField(null=True)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    transaction_status = (
        ("Pending", "Pending"),
        ("Paid", "Paid"),
        ("Completed", "Completed"),
        ("Rejected", "Rejected"),
    )

    created_date = models.DateTimeField(auto_now_add=True, null=True) 
    user = models.ForeignKey("users.User", on_delete=models.SET_NULL,null=True)
    payment_providers_txn_id = models.CharField(max_length=100, null=True)
    payment_method_name = models.CharField(max_length=100, null=True)
    discount = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    status = models.CharField(
        choices=transaction_status,
        max_length=20,
        default="Pending",
    )

    billing_address = models.ForeignKey(
        BillingAddress, on_delete=models.SET_NULL, null=True,blank=True
    )
    total_amount =  models.DecimalField(max_digits=15, decimal_places=2,null=True)
    # contact person info
    contact_name = models.CharField(max_length=50, blank=True, null=True)
    contact_email = models.CharField(max_length=100, blank=True, null=True)
    contact_mobile = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f"{self.payment_method_name}-{self.payment_providers_txn_id}"

#class SearchHistory(models.Model):
#    airline = models.ForeignKey(Airline, on_delete=models.CASCADE )
#    arrival = models.ForeignKey(City, on_delete=models.CASCADE )
#    user = models. 

class PassengerInfo(models.Model):
    booking = models.ForeignKey(
        AirlineSchedule, on_delete=models.CASCADE, null=True, blank=True
    )
    full_name = models.CharField(max_length=50, null=True, blank=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    nationality = models.CharField(max_length=50)
    age_group = models.CharField(max_length=50)
    gender = models.CharField(max_length=50,null=True,blank=True)
    passenger_title = models.CharField(max_length=50,null=True,blank=True)

    # ticket_no = models.CharField(null=True, blank=True, max_length=50)
    # pnr_no = models.CharField(null=True, blank=True, max_length=50)
    # tax_amount = models.CharField(max_length=50, null=True)
    # rate = models.CharField(max_length=20, null=True)


class FlightSupportBookingTicket(TimeStampedModel):
    status_choices = (
        ("Open", "Open"),
        ("Closed", "Closed"),
    )
    ticket_type_choices = (
        ("Cancellation", "Cancellation"),
        ("Close Date Reschedule", "Close Date Reschedule"),
        ("Open Date Reschedule", "Open Date Reschedule"),
    )
    booking = models.ForeignKey(
       Booking , on_delete=models.CASCADE, null=True, blank=True
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(choices=status_choices, max_length=10)
    ticket_type = models.CharField(choices=ticket_type_choices, max_length=30)
    reason = models.CharField(max_length=100, null=True)
    reschedule_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{str(self.booking)} S_id: {str(self.id) }"


class FlightSupportBookingTicketLog(TimeStampedModel):
    ticket = models.ForeignKey(FlightSupportBookingTicket, on_delete=models.CASCADE)
    details = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class ReserveFlightInfoTrack(TimeStampedModel):
    guid= models.CharField(max_length=90, unique=True)
    reserved_by =models.ForeignKey(User, on_delete=models.CASCADE)
    flight_id = models.CharField(max_length=90, unique=True)
    return_flight_id = models.CharField(max_length=90, unique=True,null=True,blank=True)


    def save(self, *args, **kwargs):
        if not self.guid:
            guid = str(uuid.uuid4())
            has_guid = ReserveFlightInfoTrack.objects.filter(guid=guid).exists()
            count = 1
            while has_guid:
                count += 1
                guid = str(uuid.uuid4()) + "-" + str(count)
                has_guid = ReserveFlightInfoTrack.objects.filter(guid=guid).exists()
            self.guid = guid
        super().save(*args, **kwargs)

    @property
    def give_duration_in_milliseconds(self):
        try:
            from django.utils import timezone
            date_created = self.date_created
            current_datetime = timezone.now()
            b=current_datetime-date_created
            max_seconds = 10 *60
            return int(max_seconds - b.total_seconds())*1000
        except:
            return 0 

