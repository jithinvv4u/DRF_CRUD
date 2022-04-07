from rest_framework import viewsets
from .serializers import CartSerialzer, CustomerSerializer, PlacedOrderSerializer, ProductSerializer
from orm.models import Cart, Customers, Placed_orders, Products

class CustomerViewset(viewsets.ModelViewSet):
    queryset=Customers.objects.all()
    serializer_class=CustomerSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset=Products.objects.all()
    serializer_class=ProductSerializer
    
class CartViewSet(viewsets.ModelViewSet):
    queryset=Cart.objects.all()
    serializer_class=CartSerialzer

class PlacedOrderViewSet(viewsets.ModelViewSet):
    queryset=Placed_orders.objects.all()
    serializer_class=PlacedOrderSerializer
    