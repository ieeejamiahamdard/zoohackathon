from django.shortcuts import render
from .models import AnimalDb, AnimalProduct
# Create your views here.

def animal_list(request):
    animals_list = AnimalDb.objects.all()

    context = {
        "object_list": animals_list,
    }
    return render(request, 'list.html', context)

def post_detail(request, slug=None):
    
	return render(request, "detail.html", context)