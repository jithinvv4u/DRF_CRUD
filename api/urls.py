from django.contrib import admin
from django.urls import path,include
from .views import CartDetail, CartView,CustomerView, PlacedOrdersView, ProductDetail, ProductView
urlpatterns = [
    path('customer/',CustomerView.as_view()),
    
    path('product/',ProductView.as_view()),
    path('product/<int:pk>/',ProductDetail.as_view()),
    
    path('cart/',CartView.as_view()),
    path('cart/<int:pk>/',CartDetail.as_view()),
    
    path('placed_order/',PlacedOrdersView.as_view()),
]
