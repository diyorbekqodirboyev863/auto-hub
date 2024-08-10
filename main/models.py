from django.db import models
from . import choices

class Car(models.Model):
    '''Model for car information.'''
    make = models.CharField(max_length=128)
    model = models.CharField(max_length=128)

    def save(self, *args, **kwargs):
        # Convert the model field to uppercase before saving.
        self.model = self.model.upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.make} {self.model}"

# Details.
class Detail(models.Model):
    '''Model for car details.'''
    car = models.ForeignKey(to=Car, on_delete=models.CASCADE, related_name='detail')
    car_type = models.CharField(max_length=50, choices=choices.CAR_TYPES, default=choices.CAR_TYPES[0][0])
    exterior_type = models.CharField(max_length=50, choices=choices.EXTERIOR_TYPES, default=choices.EXTERIOR_TYPES[0][0])
    vin = models.CharField(max_length=128)
    miles = models.IntegerField()
    interior_type = models.CharField(max_length=50, choices=choices.INTERIOR_TYPES, default=choices.INTERIOR_TYPES[0][0])
    stock = models.CharField(max_length=50)
    drive_type = models.CharField(max_length=50, choices=choices.DRIVE_TYPES, default=choices.DRIVE_TYPES[0][0])
    engine_type = models.CharField(max_length=50, choices=choices.ENGINE_TYPES, default=choices.ENGINE_TYPES[0][0])
    transmission_type = models.CharField(max_length=50, choices=choices.TRANSMISSION_TYPES, default=choices.TRANSMISSION_TYPES[0][0])
    color = models.CharField(max_length=50)
    mpg = models.DecimalField(max_digits=10,decimal_places=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    year = models.IntegerField(choices=choices.YEAR_CHOICES)

    def save(self, *args, **kwargs):
        # Convert the model field to uppercase before saving.
        self.color = self.color.title()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.car_type} - {self.year}'

class Feature(models.Model):
    '''Model for car feature.'''
    car = models.ForeignKey(to=Car, on_delete=models.CASCADE, related_name='feature')
    awd_4wd = models.BooleanField(default=False, verbose_name="AWD/4WD Availability")
    navigation_system = models.BooleanField(default=False, verbose_name="Navigation System Availability")
    leather_seats = models.BooleanField(default=False, verbose_name="Leather Seats Availability")
    sunroof_moonroof = models.BooleanField(default=False, verbose_name="Sunroof/Moonroof Availability")
    panoramic_roof = models.BooleanField(default=False, verbose_name="Panoramic Roof Availability")
    third_row_seating = models.BooleanField(default=False, verbose_name="Third-Row Seating Availability")
    premium_package = models.BooleanField(default=False, verbose_name="Premium Package Availability")
    oversized_wheels = models.BooleanField(default=False, verbose_name="Oversized Wheels (20-inch+) Availability")
    four_doors = models.BooleanField(default=False, verbose_name="Four Doors Availability")
    android_auto = models.BooleanField(default=False, verbose_name="Android Auto Availability")
    apple_carplay = models.BooleanField(default=False, verbose_name="Apple CarPlay Availability")
    auto_climate_control = models.BooleanField(default=False, verbose_name="Auto Climate Control Availability")
    automatic_headlights = models.BooleanField(default=False, verbose_name="Automatic Headlights Availability")
    blind_spot_monitor = models.BooleanField(default=False, verbose_name="Blind Spot Monitor Availability")
    bluetooth = models.BooleanField(default=False, verbose_name="Bluetooth Availability")
    collision_avoidance = models.BooleanField(default=False, verbose_name="Collision Avoidance Availability")
    compact_disc_player = models.BooleanField(default=False, verbose_name="Compact Disc Player Availability")
    cruise_control = models.BooleanField(default=False, verbose_name="Cruise Control Availability")
    electric_folding_rear_seats = models.BooleanField(default=False, verbose_name="Electric Folding Rear Seats Availability")
    foglights = models.BooleanField(default=False, verbose_name="Foglights Availability")
    heated_mirrors = models.BooleanField(default=False, verbose_name="Heated Mirrors Availability")
    heated_seats = models.BooleanField(default=False, verbose_name="Heated Seats Availability")
    heated_steering_wheel = models.BooleanField(default=False, verbose_name="Heated Steering Wheel Availability")
    heated_cooled_seats = models.BooleanField(default=False, verbose_name="Heated/Cooled Seats Availability")
    lane_departure_warning = models.BooleanField(default=False, verbose_name="Lane Departure Warning Availability")
    led_headlights = models.BooleanField(default=False, verbose_name="LED Headlights Availability")
    luggage_rack = models.BooleanField(default=False, verbose_name="Luggage Rack Availability")
    power_door_locks = models.BooleanField(default=False, verbose_name="Power Door Locks Availability")
    power_driver_seat = models.BooleanField(default=False, verbose_name="Power Driver Seat Availability")
    power_mirrors = models.BooleanField(default=False, verbose_name="Power Mirrors Availability")
    power_passenger_seat = models.BooleanField(default=False, verbose_name="Power Passenger Seat Availability")
    power_tilt_wheel = models.BooleanField(default=False, verbose_name="Power Tilt Wheel Availability")
    power_windows = models.BooleanField(default=False, verbose_name="Power Windows Availability")
    premium_sound_system = models.BooleanField(default=False, verbose_name="Premium Sound System Availability")
    privacy_glass = models.BooleanField(default=False, verbose_name="Privacy Glass Availability")
    push_button_start = models.BooleanField(default=False, verbose_name="Push Button Start Availability")

    def __str__(self):
        return self.car.model


# Images.
class Image(models.Model):
    '''Model for car images.'''
    detail = models.ForeignKey(to=Car, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='cars/')



