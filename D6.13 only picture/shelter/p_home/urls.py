from django.urls import path

from  . import views

urlpatterns = [
    path('', views.Animal.as_view(), name='animal_list')

]