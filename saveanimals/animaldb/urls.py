from django.urls import path, include
from .views import animal_list
urlpatterns = [

    path('', animal_list, name="animal_list"),
]
