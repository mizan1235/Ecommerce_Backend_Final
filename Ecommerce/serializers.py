# serializers.py
from rest_framework import serializers
from .models import product_details,orders


class FilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = product_details
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = orders
        fields = '__all__'