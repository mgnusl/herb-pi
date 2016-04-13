from django.forms import ModelForm
from django import forms
from plants.models import PlantInstance


class PlantInstanceForm(ModelForm):
    class Meta:
        model = PlantInstance
        fields = ['plant_type']
    def __init__(self, *args, **kwargs):
        super(PlantInstanceForm, self).__init__(*args, **kwargs)

        pin_choices = ( (x,str(x)) for x in range(8))
        self.fields['pin_number'] = forms.ChoiceField(choices = pin_choices, initial=self.instance.pin_number)
