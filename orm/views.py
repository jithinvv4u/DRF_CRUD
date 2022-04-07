from itertools import count, product
from django.shortcuts import redirect, render
from .models import Products,Colors,Size,Brands,Customers,Placed_orders,Cart
from django.db.models import F,Count,Max,Sum
# Create your views here.

def task1(request):
    #1.Get all available products of addidas brand
    adidas=Products.objects.filter(product_brand_id__brand_name='Adidas') #1
    #2.Get all shoe brand name
    shoe_brands=Products.objects.filter(product_name='Shoe').values_list('product_brand_id__brand_name') #2
    #3.Get count of products available in puma brand
    count_puma=Products.objects.filter(product_brand_id__brand_name='puma').count() #3
    #4.get available quantity of Raymond white color shirt in products
    count_raymond_white=Products.objects.filter(product_brand_id__brand_name='Raymond',product_color_id__color_name='white',product_name='Shirt').count() #4 inc
    
    #5.which brand having max products, get their products also
    most_brand=Products.objects.filter().values('product_brand_id').annotate(Count('product_brand_id')).aggregate(Max('product_brand_id__count'))  #5 inc
    top_brand=Products.objects.filter().values('')
    # top_brand=Products.objects.filter().order_by('product_brand_id').aggregate(Count('product_brand_id'))
    
    #6.get laptop brand whose price is greater than 40000
    laptop_gt40k=Products.objects.filter(product_name='laptop',product_price__gt=40000).values_list('product_brand_id__brand_name') #6
    #7.get the list of brands those doesn't have products
    null_brand=Brands.objects.exclude(brand_id__in=Products.objects.filter().values('product_brand_id')).values_list('brand_name')
    #8.get all the produts added on january
    jan_product=Products.objects.filter(product_added_date__month='01') #8
    #9.get shoe brands whose price between 1500 to 2000
    Shoe_brand_btw=Products.objects.filter(product_name='Shoe',product_price__gt=1500,product_price__lt=2000).values_list('product_brand_id__brand_name')  #9
    print(most_brand)
 
    return render(request,'task1.html')


def task2(request):
    #1. Total order placed between feb 15 to 28 and the details like,
    #    - total orders amount
    #    - name of item ordered most by the users
    #    - customer who placed max order between these dates
    total_order_feb15_28=Placed_orders.objects.filter(placed_order_date__gt='2022-02-15',placed_order_date__lt='2022-02-28').aggregate(total_order=Count('placed_order_id'))
    
    total_amout_feb15_28=Placed_orders.objects.filter(placed_order_date__gt='2022-02-15',placed_order_date__lt='2022-02-28').aggregate(Sum('placed_order_total_amount'))
    name_item_feb15_28=Cart.objects.filter(cart_item_placed_id__placed_order_date__gt='2022-02-15',cart_item_placed_id__placed_order_date__lt='2022-02-28').values('cart_item_name').annotate(count=Count('cart_product_id')).order_by('-count')[:1]
    most_customer_feb15_28_2=Placed_orders.objects.filter(placed_order_date__gt='2022-02-15',placed_order_date__lt='2022-02-28').values('placed_order_user_id').annotate(placed_order=Count('placed_order_user_id')).order_by('-placed_order')[:1]
    
    # 2. active items(item status should be 1) present in the cart for the customer whose phone number is '9999988888'
    active_items=Cart.objects.filter(cart_item_user_id__customer_phone=9999988888,cart_item_status=1,).values('cart_item_name')
    # 3. get customer phone number who didn't place their first order yet
    nullproduct_cust=Customers.objects.exclude(customer_id__in=Placed_orders.objects.filter().values('placed_order_user_id')).values_list('customer_phone')
    # 4. get customer details who placed order this month(march)
    cust_placed_march=Placed_orders.objects.filter(placed_order_date__month='03').values_list('placed_order_user_id','placed_order_user_id__customer_name','placed_order_user_id__customer_phone','placed_order_user_id__customer_email','placed_order_user_id__customer_address','placed_order_user_id__customer_zip').distinct()
    # 5. get the count of customers who ordered Nike Shoe
    customerCount_nike_shoe=Cart.objects.filter(cart_product_id__product_name='Shoe',cart_product_id__product_brand_id__brand_name='Nike').values('cart_item_user_id').aggregate(count_of_customer=Count('cart_item_user_id'))
    # 6. get the customer details(email and phone number) who didn't place any order in this month(march)
    cust_notPlaced_march=Customers.objects.exclude(customer_id__in=Placed_orders.objects.filter(placed_order_date__month='03').values('placed_order_user_id').distinct()).values_list('customer_email','customer_phone')
    
    # 7. most purchased item in march
    most_purchase_march=Cart.objects.filter(cart_item_placed_id__placed_order_date__month='03').values('cart_item_name','cart_product_id__product_brand_id__brand_name').annotate(purchase_count=Count('cart_item_id')).order_by('-purchase_count')[:1]
    
    # SELECT cart_product_id, COUNT(cart_product_id) as product_count from cart_items 
    # JOIN placed_orders ON cart_item_placed_id = placed_orders.placed_order_id 
    # WHERE MONTH(placed_orders.placed_order_date) = 3 
    # GROUP BY cart_items.cart_product_id 
    # ORDER BY product_count DESC LIMIT 1
    
    # 8. did user ordered apple laptop and Raymond shirt in march?
    apple_laptop_march=Cart.objects.filter(cart_product_id__product_name='laptop',cart_product_id__product_brand_id__brand_name='Dell',cart_item_placed_id__placed_order_date__month='03').values('cart_product_id__product_brand_id__brand_name','cart_product_id__product_name').annotate(count=Count('cart_item_id'))
    raymond_shirt_march=Cart.objects.filter(cart_product_id__product_name='Shirt',cart_product_id__product_brand_id__brand_name='Raymond',cart_item_placed_id__placed_order_date__month='03').values('cart_product_id__product_brand_id__brand_name','cart_product_id__product_name').annotate(count=Count('cart_item_id'))
    
    return render(request,'task2.html')