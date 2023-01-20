from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet
from api import models, serializers
from rest_framework.generics import get_object_or_404
from json import loads, dumps

from . import models

class ProductViewSet(ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

class CategoryViewSet(ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
