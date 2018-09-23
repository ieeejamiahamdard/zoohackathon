from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AnimalDbSerializer, AnimalProductSerializer

from animaldb.models import AnimalDb, AnimalProduct

class AnimalDbView(viewsets.ModelViewSet):
    queryset = AnimalDb.objects.all()
    serializer_class = AnimalDbSerializer

class AnimalProductView(viewsets.ModelViewSet):
    queryset = AnimalProduct.objects.all()
    serializer_class = AnimalProductSerializer    