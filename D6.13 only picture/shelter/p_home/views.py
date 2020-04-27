from django.shortcuts import render
from .models import Animal, Breed
from django.template import loader
from django.views.generic import CreateView, ListView



class Animal(ListView):
    model = Animal
    templates_name = 'animal_list.html'


