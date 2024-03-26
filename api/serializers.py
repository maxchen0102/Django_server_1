from rest_framework import serializers
from product.models import Product



class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

