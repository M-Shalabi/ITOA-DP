from django import forms
from .models import Country

class CountryForm(forms.Form):
    class Meta:
        model = Country
        fields = ['name']