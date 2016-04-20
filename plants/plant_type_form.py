from django.forms import ModelForm
from plants.models import Plant


class PlantTypeForm(ModelForm):
    class Meta:
        model = Plant
        fields = ['name', 'ideal_humidity', 'sun_preference', 'shade_tolerance', 'fertilizing_interval']
