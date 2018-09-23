from django.shortcuts import render, get_object_or_404
from .models import AnimalDb, AnimalProduct
import geocoder
# Create your views here.

def animal_list(request):
    g = geocoder.ip("me")
    animals_list = AnimalDb.objects.filter(location=g.state.lower())#location=g.state.lower()
    print(g.state)
    context = {
        "object_list": animals_list,
        "location" : g.state
    }
    return render(request, 'list.html', context)

def animal_detail(request, slug=None):
    animalName = get_object_or_404(AnimalDb, slug=slug)
    # print(instance.AnimalProduct.all())
    animal_product = animalName.animal_product.all()
    context = {
        "animalName":animalName,
        "animal_product" : animal_product,
    }
    return render(request, "detail.html", context)