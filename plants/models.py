from __future__ import unicode_literals
from django.db import models


class Plant(models.Model):
    name = models.CharField(max_length=100)

    # Humidity. LOW, MODERATE, HIGH
    ideal_humidity = models.CharField(max_length=100, choices=[('LOW', 'LOW'), ('MODERATE', 'MODERATE'), ('HIGH', 'HIGH')])

    # How often the plant needs fertilizer. In days. Not required
    fertilizing_interval = models.IntegerField(default=0, blank=True,
                                               help_text="How often the plant needs fertilizer (in days)")

    # How much sun the plant prefers on a scale from 0-2. Not required.
    sun_preference = models.IntegerField(default=0, blank=True, help_text="How much sun does the plant prefer (0-2)")

    # How much shade the plant can tolerate on a scale from 0-4. Not required.
    shade_tolerance = models.IntegerField(default=0, blank=True, help_text="How much shade can the plant tolerate (0-4)")

    # Not used for now
    ideal_ph_min = models.DecimalField(max_digits=3, decimal_places=2, default=0, blank=True,
                                       help_text="Minimum ideal pH value")
    ideal_ph_max = models.DecimalField(max_digits=3, decimal_places=2, default=0, blank=True,
                                       help_text="Maximum ideal pH value")

    # image = models.ImageField(...)

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
