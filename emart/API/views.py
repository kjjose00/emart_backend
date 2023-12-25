from rest_framework import viewsets
from emart.models import Product,Category
from .serializers import CategorySerializer,ProductSerializer

class CategorySerializerViewsets(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer

class ProductSerializerViewsets(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    

