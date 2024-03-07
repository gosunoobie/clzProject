from django.db import models


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

    def __str__(self):
        return f"{self.departure_time}-{self.arrival_time}"

    @property
    def get_is_seat_available(self):
        if self.passenger_per_flight < 1:
            return False
        else:
            return True




class Booking(models.Model):

    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Pending', 'Pending'),
        ('Cancelled', 'Cancelled'),
    ]
    user = models.ForeignKey("users.User",on_delete=models.CASCADE)
    schedule = models.ForeignKey(AirlineSchedule,on_delete=models.CASCADE)
    no_of_adults = models.IntegerField()
    no_of_child = models.IntegerField()
    status = models.CharField(max_length=10,choices=STATUS_CHOICES, default="Pending" )
    transaction = models.ForeignKey("domestic_flights.transaction",on_delete=models.CASCADE,null=True)

class Transaction(models.Model):
    transaction_status = (
        ("Pending", "Pending"),
        ("Paid", "Paid"),
        ("Completed", "Completed"),
        ("Rejected", "Rejected"),
    )

    user = models.ForeignKey("users.User", on_delete=models.SET_NULL,null=True)
    payment_providers_txn_id = models.CharField(max_length=100, null=True)
    payment_method_name = models.CharField(max_length=100, null=True)
    discount = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    status = models.CharField(
        choices=transaction_status,
        max_length=20,
        default="Pending",
    )
    total_amount =  models.DecimalField(max_digits=15, decimal_places=2,null=True)

    def __str__(self):
        return f"{self.payment_method_name}-{self.payment_providers_txn_id}"

#class SearchHistory(models.Model):
#    airline = models.ForeignKey(Airline, on_delete=models.CASCADE )
#    arrival = models.ForeignKey(City, on_delete=models.CASCADE )
#    user = models. 
