from rest_framework import serializers
from emart.models import Product,Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields="__all__"
        read_only_fields=['id','name']

class ProductSerializer(serializers.ModelSerializer):
    category=CategorySerializer(read_only=True)
    class Meta:
        model=Product
        fields="__all__"
             


