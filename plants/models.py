from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Plant(models.Model):
    name = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)

    # 'Relative humidity'. x.xx
    ideal_humidity = models.DecimalField(max_digits=3, decimal_places=2, help_text="Ideal humidity (between 0 and 1")

    # How often the plant needs fertilizer. In days. Not required
    fertilizing_interval = models.IntegerField(default=0, blank=True,
                                               help_text="How often the plant needs fertilizer (in days)")

    # Not used for now
    ideal_ph_min = models.DecimalField(max_digits=3, decimal_places=2, default=0, blank=True,
                                       help_text="Minimum ideal pH value")
    ideal_ph_max = models.DecimalField(max_digits=3, decimal_places=2, default=0, blank=True,
                                       help_text="Maximum ideal pH value")

    # image = models.ImageField(...)

    def __str__(self):
        return self.name


class PlantCollection(models.Model):
    name = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
