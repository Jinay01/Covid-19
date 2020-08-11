from django.forms import ModelForm
from .models import *


class CountryInput(ModelForm):
    class Meta():
        model = Country
        fields = '__all__'
