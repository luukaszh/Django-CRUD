from django import forms
from .models import Bee


class BeeForm(forms.ModelForm):
    class Meta:
        model = Bee
        fields = ['name', 'code']