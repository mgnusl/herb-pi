from django.forms import ModelForm
from plants.models import PlantInstance

class PlantInstanceForm(ModelForm):
    class Meta:
        model = PlantInstance
        fields = ['plant_type', 'pin_number']
