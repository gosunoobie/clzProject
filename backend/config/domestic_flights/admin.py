from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Airline)
class AirlineAdmin(admin.ModelAdmin):
    list_display = ('id','code', 'name',)

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id','city_name', 'city_code',)

@admin.register(AirlineRoute)
class AirlineRouteAdmin(admin.ModelAdmin):
    list_display = ('id','airline','arrival','destination','flights_per_day' )

@admin.register(AirlineSchedule)
class AirlineScheduleAdmin(admin.ModelAdmin):
    list_display = ('id','airline_route','passenger_per_flight','departure_time','arrival_time',  )


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id','user','schedule','transaction','no_of_adults','no_of_child','status', 'created_date' )


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id','user','status','payment_method_name','total_amount','created_date'  )


admin.site.register(PassengerInfo)
admin.site.register(FlightSupportBookingTicket)
admin.site.register(FlightSupportBookingTicketLog)
admin.site.register(ReserveFlightInfoTrack)
admin.site.register(BillingAddress)
admin.site.register(WeekDays)

