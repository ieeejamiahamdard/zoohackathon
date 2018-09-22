from django.db import models

# Create your models here.

class AnimalDb(models.Model):
    name = models.CharField(max_length=25, null=False)
    location = models.CharField(max_length=10, null=False)
    # slug = models.SlugField(unique=True)
    def __str__(self):
        return self.name

class AnimalProduct(models.Model):
    name = models.CharField(max_length=25, null=False)
    animal = models.ManyToManyField(AnimalDb)
    details = models.TextField()

    def __str__(self):
        return self.name