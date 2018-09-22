from django.shortcuts import render, get_object_or_404
from .models import AnimalDb, AnimalProduct
# Create your views here.

def animal_list(request):
    animals_list = AnimalDb.objects.all()

    context = {
        "object_list": animals_list,
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