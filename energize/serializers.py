from rest_framework import serializers
from .models import Drink

class DrinkSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
       model = Drink
       fields = ('id', 'image_url', 'caffeine_content', 'name', 'price', 'extra_ingredients')