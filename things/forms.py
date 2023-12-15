from django import forms
from .models import Thing

class ThingForm(forms.Modelform):
    model = Thing
    fields = {"name", "description", "quantity"}
    widgets = {'description':forms.Textarea()}
    
