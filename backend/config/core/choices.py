
TIME_CHOICES = (
    ("Per Hour", "Per Hour"),
    ("Per Day", "Per Day"),
    ("Per Ticket", "Per Ticket"),
)


INVENTORY_TIME_CHOICES = (
    ("Per Hour", "Per Hour"),
    ("Per Day", "Per Day"),
    ("No Time Needed", "No Time Needed"),
    ("Per Fix Duration", "Per Fix Duration"),
)


NATIONALITY_CHOICES = (
    ("Nepali", "Nepali"),
    ("Foreigners", "Foreigners"),
)
AGE_CHOICES = (
    ("Child", "Child"),
    ("Adult", "Adult"),
)


LOYALTY_COIN_CHOICES = (
    ("ACTIVE", "ACTIVE"),
    ("EXPIRED", "EXPIRED"),
    ("REDEEMED", "REDEEMED"),
)

ELIGIBLE_TIME_UNIT = (
    ("Hour", "Hour"),
    ("Day", "Day"),
)

AIRLINE_CHOICES = (
    ("Nepal Airlines", "Nepal Airlines"),
    ("Tara Air", "Tara Air"),
    ("Yeti Airlines", "Yeti Airlines"),
    ("Summit Air", "Summit Air"),
    ("Sita Air", "Sita Air"),
    ("Buddha Air", "Buddha Air"),
    ("Guna Airlines", "Guna Airlines"),
    ("Shree Airlines", "Shree Airlines"),
    ("Saurya Airlines", "Saurya Airlines"),
    ("Simrik Airlines", "Simrik Airlines"),
)
BOOKING_STATUS = (
    ("PENDING", "PENDING"),
    ("ACTIVE", "ACTIVE"),
    # ("COMPLETED", "COMPLETED"),
    ("CANCELLED", "CANCELLED"),
)

REQUEST_CHOICES = (
    ("GET","GET"),
    ("POST","POST"),
)
