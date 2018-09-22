from django.db import models
from django.urls import reverse
# Create your models here.

class AnimalProduct(models.Model):
    name = models.CharField(max_length=25, null=False)
    details = models.TextField()

    def __str__(self):
        return self.name

class AnimalDb(models.Model):
    name = models.CharField(max_length=25, null=False)
    location = models.CharField(max_length=10, null=False)
    slug = models.SlugField()
    animal_product = models.ManyToManyField(AnimalProduct)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("animaldb:animal_detail", kwargs={"slug": self.slug})
