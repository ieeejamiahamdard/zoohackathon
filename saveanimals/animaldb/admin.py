from django.contrib import admin
from .models import AnimalDb, AnimalProduct
# Register your models here.

admin.site.register(AnimalDb)
admin.site.register(AnimalProduct)