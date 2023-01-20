from rest_framework import serializers

from api import models

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(read_only=True, many=True)
    class Meta:
        model = models.Category
        fields = '__all__'