from django import forms
from .models import Animal, Breed

class AnimalForm(forms.ModelForm):

    class Meta:
        model = Animal
        fields = '__all__'

