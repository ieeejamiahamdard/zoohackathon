from django.db import models
from django.urls import reverse
# Create your models here.


def upload_location(instance, filename):
    """
    instance.__class__ gets the model Post. We must use this method because the model is defined below.
    Then create a queryset ordered by the "id"s of each object,
    Then we get the last object in the queryset with `.last()`
    Which will give us the most recently created Model instance
    We add 1 to it, so we get what should be the same id as the the post we are creating.
    """
    return "%s/%s" %(instance.id, filename)

class AnimalProduct(models.Model):
    name = models.CharField(max_length=100, null=False)
    details = models.TextField()
    image = models.ImageField(upload_to=upload_location,
            null=True,
            blank=True,
            width_field="width_field",
            height_field="height_field")
    height_field = models.IntegerField(default=400)
    width_field = models.IntegerField(default=500)
    def __str__(self):
        return self.name

class AnimalDb(models.Model):
    name = models.CharField(max_length=100, null=False)
    location = models.CharField(max_length=100, null=False)
    slug = models.SlugField()
    animal_product = models.ManyToManyField(AnimalProduct)
    image = models.ImageField(upload_to=upload_location,
            null=True,
            blank=True,
            width_field="width_field",
            height_field="height_field")
    height_field = models.IntegerField(default=400)
    width_field = models.IntegerField(default=500)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("animaldb:animal_detail", kwargs={"slug": self.slug})
