from rest_framework import serializers
from animaldb.models import AnimalProduct, AnimalDb

class AnimalDbSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = AnimalDb 
        fields = (
                'name',
                'slug',
                'id',
                'location',
                'animal_product',
                'image',

                )

class AnimalProductSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = AnimalProduct
        fields = (
            'name',
            'id',
            'details',
            'image',
        )