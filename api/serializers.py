from rest_framework import serializers
from orm.models import Customers,Products,Cart,Placed_orders

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customers
        fields='__all__'
    
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields='__all__'
        
class CartSerialzer(serializers.ModelSerializer):
    class Meta:
        model=Cart
        fields='__all__'

class PlacedOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Placed_orders
        fields='__all__'
        
