from rest_framework import serializers
from plants.models import Plant


class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = (
            'id', 'name', 'date_created', 'ideal_humidity', 'fertilizing_interval', 'ideal_ph_min', 'ideal_ph_max')
