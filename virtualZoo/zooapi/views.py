from django.shortcuts import render
from rest_framework import generics
from .serializers import ItemSerializer
from .models import Animal

class AnimalList(generics.ListAPIView):
    queryset = Animal.objects.all()
    serializer_class = ItemSerializer


class AnimalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Animal.objects.all()
    serializer_class = ItemSerializer

class AnimalCreate(generics.CreateAPIView):
    queryset = Animal.objects.all()
    serializer_class = ItemSerializer


""" Concrete View Classes -> delete this before committing!!!
#CreateAPIView
Used for create-only endpoints.
#ListAPIView
Used for read-only endpoints to represent a collection of model instances.
#RetrieveAPIView
Used for read-only endpoints to represent a single model instance.
#DestroyAPIView
Used for delete-only endpoints for a single model instance.
#UpdateAPIView
Used for update-only endpoints for a single model instance.
##ListCreateAPIView
Used for read-write endpoints to represent a collection of model instances.
RetrieveUpdateAPIView
Used for read or update endpoints to represent a single model instance.
#RetrieveDestroyAPIView
Used for read or delete endpoints to represent a single model instance.
#RetrieveUpdateDestroyAPIView
Used for read-write-delete endpoints to represent a single model instance.
"""