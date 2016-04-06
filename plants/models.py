from __future__ import unicode_literals
from django.db import models


class Plant(models.Model):
    name = models.CharField(max_length=100)

    # Humidity. LOW, MODERATE, HIGH
    ideal_humidity = models.CharField(max_length=100, choices=[('LOW', 'LOW'), ('MODERATE', 'MODERATE'), ('HIGH', 'HIGH')])

    # How much sun the plant prefers. Not required.
    sun_preference = models.CharField(max_length=100, blank=True, help_text="How much sun the plant prefers",
                                      choices=[('MINIMAL', 'MINIMAL'), ('FULL', 'FULL')])

    # How much shade the plant can tolerate. Not required.
    shade_tolerance = models.CharField(max_length=100, blank=True, help_text="How much shade the plant can tolerate",
                                       choices=[('NONE', 'NONE'), ('LIGHT', 'LIGHT'), ('PERMANENT', 'PERMANENT')])

    # How often the plant needs fertilizer. In days. Not required
    fertilizing_interval = models.IntegerField(default=0, blank=True,
                                               help_text="How often the plant needs fertilizer (in days)")

    # Not used for now
    ideal_ph_min = models.DecimalField(max_digits=3, decimal_places=2, default=-1, blank=True,
                                       help_text="Minimum ideal pH value")
    ideal_ph_max = models.DecimalField(max_digits=3, decimal_places=2, default=-1, blank=True,
                                       help_text="Maximum ideal pH value")

    def __str__(self):
        return self.name


class PlantInstance(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    plant_type = models.ForeignKey(Plant)
    sensor_offset_max = models.IntegerField(help_text="Humidity sensor offset for calibration (max)", default=0)
    sensor_offset_min = models.IntegerField(help_text="Humidity sensor offset for calibration (min)", default=0)
    pin_number = models.IntegerField(help_text="Pin number of the humidity sensor", default=0)

    def __str__(self):
        return str(self.plant_type.name)


class MoistureLog(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    moisture_level = models.IntegerField(default=0)
    plant_instance = models.ForeignKey(PlantInstance, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.date)


class WateringLog(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    num_seconds_open = models.IntegerField()
    plant_instance = models.ForeignKey(PlantInstance, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.date)
