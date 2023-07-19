from django.shortcuts import render

from .models import Product
from .serializers import Productserializers
from rest_framework import generics

# Create your views here.

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = Productserializers


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = Productserializers