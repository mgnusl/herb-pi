from rest_framework import serializers
from plants.models import *


class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = (
            'id', 'name', 'ideal_humidity', 'fertilizing_interval',
            'sun_preference', 'shade_tolerance', 'ideal_ph_min', 'ideal_ph_max'
        )


class MoistureLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoistureLog
        fields = (
            'date', 'moisture_level'
        )


class WateringLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = WateringLog
        fields = (
            'date', 'num_seconds_open'
        )


class PlantInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantInstance
        fields = (
            'date_created', 'plant_type', 'sensor_offset_max', 'sensor_offset_min'
        )
