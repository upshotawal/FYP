from django.db.models import fields
from rest_framework import serializers #truns the sql format files that we created in models o json format files
from .models import Category
from .models import Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','name', 'slug')
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id','category', 'created_by', 'title', 'author', 'description',
                  'image', 'slug', 'in_stock', 'is_active', 'created', 'update')