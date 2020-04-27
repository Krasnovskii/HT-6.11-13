from django.contrib import admin

from .models import Animal, Breed, Type

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    pass

@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    pass

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    pass