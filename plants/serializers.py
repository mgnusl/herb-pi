from rest_framework import serializers
from plants.models import Plant
from plants.models import MoistureLog


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
