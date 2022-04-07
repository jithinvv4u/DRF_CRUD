from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import CartSerialzer, CustomerSerializer, PlacedOrderSerializer, ProductSerializer
from orm.models import Cart, Customers, Placed_orders, Products
# Create your views here.

class CustomerView(APIView):
    def get(self,request):
        queryset=Customers.objects.all()
        serializer=CustomerSerializer(queryset, many=True)
        return Response(serializer.data)
        
   
class ProductView(APIView):
    def get(self, request, format=None):
        queryset = Products.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class ProductDetail(APIView):
    def get_object(self, pk):
        try:
            return Products.objects.get(pk=pk)
        except Products.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = ProductSerializer(queryset)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = ProductSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        queryset = self.get_object(pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
        
class CartView(APIView):
    def get(self, request, format=None):
        queryset = Cart.objects.all()
        serializer = CartSerialzer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CartSerialzer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class CartDetail(APIView):
    def get_object(self, pk):
        try:
            return Cart.objects.get(pk=pk)
        except Cart.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = CartSerialzer(queryset)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = CartSerialzer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        queryset = self.get_object(pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class PlacedOrdersView(APIView):
    def get(self,request,*args,**kwargs):
        queryset=Placed_orders.objects.all()
        serializer=PlacedOrderSerializer(queryset, many=True)
        return Response(serializer.data)
    
    
        
        
        
        
        
# class CartView(APIView):
#     def get(self,request,*args,**kwargs):
#         queryset=Cart.objects.all()
#         serializer=CartSerialzer(queryset, many=True)
#         return Response(serializer.data)

# class CartCreateView(APIView):
#     def post(self,request,*args,**kwargs):
#         serializer=CartSerialzer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)

# class CartUpdateView(APIView):
#     def get_object(self,pk):
#         try:
#             return Cart.objects.grt(pk=pk)
#         except Cart.DoesNotExist:
#             raise Http404
    
#     def put(self,request,pk,format=None):
#         cart=Cart.get_object(pk)
#         serializer=CartSerialzer(cart,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)