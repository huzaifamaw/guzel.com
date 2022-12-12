from rest_framework import serializers
from .models import TbCustomer, TbProductCategory, TbOrder, TbProduct

class ProductCategory(serializers.ModelSerializer):
    class Meta:
        model = TbProductCategory
        fields = '__all__'

class customers(serializers.ModelSerializer):
    class Meta:
        model = TbCustomer
        fields = '__all__'

class Product(serializers.ModelSerializer):
    class Meta:
        model = TbProduct
        fields = '__all__'

class Order(serializers.ModelSerializer):
    class Meta:
        model = TbOrder
        fields = '__all__'