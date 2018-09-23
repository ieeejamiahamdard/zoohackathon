from django.urls import path, include
from rest_framework import routers
from .views import AnimalDbView, AnimalProductView

router = routers.DefaultRouter()
router.register('report',AnimalDbView)
router.register('animalsproducts',AnimalProductView)

urlpatterns = [
    path('',include(router.urls)),
]