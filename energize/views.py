from rest_framework import generics
from .serializers import DrinkSerializer
from .models import Drink

class DrinkList(generics.ListCreateAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer

class DrinkDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer