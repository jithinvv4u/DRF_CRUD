from django import db
from django.db import models

# Create your models here.
        
class Brands(models.Model):
    brand_id=models.IntegerField(primary_key=True)
    brand_name=models.CharField(max_length=45)
    brand_status=models.BooleanField()
    
    class Meta:
        managed=False
        db_table='brands'
        
class Colors(models.Model):
    color_id=models.IntegerField(primary_key=True)
    color_name=models.CharField(max_length=45)
    parent_color=models.CharField(max_length=45)
        
    class Meta:
        managed=False
        db_table='colors'

class Size(models.Model):
    size_id=models.IntegerField(primary_key=True)
    size_value=models.CharField(max_length=45)
    size_measurement=models.CharField(max_length=45)
    
    class Meta:
        managed=False
        db_table='sizes'
            
class Products(models.Model):
    product_id=models.IntegerField(primary_key=True)
    product_name=models.CharField(max_length=45)
    product_price=models.IntegerField()
    product_available_qty=models.IntegerField()
    product_status=models.IntegerField()
    product_added_date=models.DateField()
    product_brand_id=models.ForeignKey(Brands,on_delete=models.CASCADE,db_column='product_brand_id')
    product_color_id=models.ForeignKey(Colors,on_delete=models.CASCADE,db_column='product_color_id')
    product_size_id=models.ForeignKey(Size,on_delete=models.CASCADE,db_column='product_size_id')
    
    class Meta:
        managed=False
        db_table='Products'
        
    def __str__(self):
        return self.product_name
    
    
class Customers(models.Model):
    customer_id=models.IntegerField(primary_key=True)
    customer_name=models.CharField(max_length=45)
    customer_phone=models.CharField(max_length=45)
    customer_email=models.CharField(max_length=45)
    customer_address=models.CharField(max_length=45)
    customer_zip=models.IntegerField()
    customer_status=models.BooleanField()
    
    class Meta:
        managed=False
        db_table='customers'
        
    def __str__(self):
        return self.customer_name
        
class Placed_orders(models.Model):
    placed_order_id=models.IntegerField(primary_key=True)
    placed_order_user_id=models.ForeignKey(Customers,on_delete=models.CASCADE,db_column='placed_order_user_id')
    placed_order_date=models.DateTimeField()
    placed_order_total_amount=models.IntegerField()
    placed_order_delivery_status=models.BooleanField()
    
    class Meta:
        managed=False
        db_table='placed_orders'
        
class Cart(models.Model):
    cart_item_id=models.IntegerField(primary_key=True)
    cart_product_id=models.ForeignKey(Products,on_delete=models.CASCADE,db_column='cart_product_id')
    cart_item_name=models.CharField(max_length=45)
    cart_item_user_id=models.ForeignKey(Customers,on_delete=models.CASCADE,db_column='cart_item_user_id')
    cart_item_quantity=models.IntegerField()
    cart_item_price=models.IntegerField()
    cart_item_status=models.BooleanField()
    cart_item_placed_id=models.ForeignKey(Placed_orders,on_delete=models.CASCADE,db_column='cart_item_placed_id')
    
    class Meta:
        managed=False
        db_table='cart_items'
            
    def __str__(self):
        return self.cart_item_name
        