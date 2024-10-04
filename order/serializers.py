from rest_framework import serializers
from .models import Order

class OrderItemsSerializer(serializers.ModelSerializer):
    ...