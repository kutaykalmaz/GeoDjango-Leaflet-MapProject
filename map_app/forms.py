from django import forms
from django.forms import fields, widgets
from .models import MarkedPlaces
from leaflet.forms.widgets import LeafletWidget

class MarkForm(forms.ModelForm):
    class Meta:
        model = MarkedPlaces
        fields = ('name', 'location')
        widgets = {'location' : LeafletWidget()}