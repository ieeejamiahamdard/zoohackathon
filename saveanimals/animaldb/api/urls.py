from django.urls import path, include
from rest_framework import routers
from .views import AnimalDbView, AnimalProductView

router = routers.DefaultRouter()
router.register('animalsdata',AnimalDbView)
router.register('animalsproducts',AnimalProductView)

urlpatterns = [
    path('',include(router.urls)),
]