from rest_framework import serializers
from .models import Product, Order, OrderItem

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'name',
            'description',
            'price',
            'stock',
        )
        
    # custom field level validation
    def validate_price(self, value): # validate_<field_name>(self, value)
        """
        Validate the product price.
        """
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than 0.")
        return value