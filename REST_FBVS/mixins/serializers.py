from dataclasses import fields
from rest_framework import serializers
from mixins.models import ProductsModel

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductsModel
        fields = ['id', 'name', 'unit', 'price']

        