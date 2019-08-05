from django import forms
from django.contrib.gis import forms
from leaflet.forms.widgets import LeafletWidget
from .models import Pet


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'address', 'city', 'pet_image', 'location']
        widgets = {'location': LeafletWidget()}
