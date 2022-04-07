from django.shortcuts import redirect, render
from .models import Products,Colors,Size,Brands,Customers,Placed_orders,Cart
from django.db.models import F,Count,Max,Sum

def task2(request):
    #1. Total order placed between feb 15 to 28 and the details like,
    total_order_feb15_28=Placed_orders.objects.filter(placed_order_date__gt='2022-02-15',placed_order_date__lt='2022-02-28').aggregate(total_order=Count('placed_order_id'))
    # {'total_order': 4}
        
    #    - total orders amount
    total_amout_feb15_28=Placed_orders.objects.filter(placed_order_date__gt='2022-02-15',placed_order_date__lt='2022-02-28').aggregate(Sum('placed_order_total_amount'))
    # {'placed_order_total_amount__sum': 4808}
        
    #    - name of item ordered most by the users
    name_item_feb15_28=Cart.objects.filter(cart_item_placed_id__placed_order_date__gt='2022-02-15',cart_item_placed_id__placed_order_date__lt='2022-02-28').values('cart_item_name').annotate(count=Count('cart_product_id')).order_by('-count')[:1]
    # <QuerySet [{'cart_item_name': 'Bag', 'count': 2}]>
    
    #    - customer who placed max order between these dates
    most_customer_feb15_28_2=Placed_orders.objects.filter(placed_order_date__gt='2022-02-15',placed_order_date__lt='2022-02-28').values('placed_order_user_id').annotate(placed_order=Count('placed_order_user_id')).order_by('-placed_order')[:1]
    # <QuerySet [{'placed_order_user_id': 6, 'placed_order': 2}]>
    
    # 2. active items(item status should be 1) present in the cart for the customer whose phone number is '9999988888'
    active_items=Cart.objects.filter(cart_item_user_id__customer_phone=9999988888,cart_item_status=1,).values('cart_item_name')
    # <QuerySet [{'cart_item_name': 'Shirt'}, {'cart_item_name': 'shoe'}, {'cart_item_name': 'Shoe'}, {'cart_item_name': 'Laptop'}]>
    
    # 3. get customer phone number who didn't place their first order yet
    nullproduct_cust=Customers.objects.exclude(customer_id__in=Placed_orders.objects.filter().values('placed_order_user_id')).values_list('customer_phone')
    # <QuerySet [('8555599999',)]>
    
    # 4. get customer details who placed order this month(march)
    cust_placed_march=Placed_orders.objects.filter(placed_order_date__month='03').values_list('placed_order_user_id','placed_order_user_id__customer_name','placed_order_user_id__customer_phone','placed_order_user_id__customer_email','placed_order_user_id__customer_address','placed_order_user_id__customer_zip').distinct()
    # <QuerySet [(3, 'Lara', '67777555555', 'lara@gmail.com', '3rd Avenue, Trivandrum ', 695004), (4, 'Anu', '6555522222', 'anu@gmail.com', '4th Avenue, Trivandrum', 695022), (1, 'John', '9999988888', 'john@gmail.com', '1st Avenue, Kochi ', 682017), (2, 'Mathew', '9888899999', 'mathew@gmail.com', '2st Avenue, Kochi ', 682034)]>
    
    # 5. get the count of customers who ordered Nike Shoe
    customerCount_nike_shoe=Cart.objects.filter(cart_product_id__product_name='Shoe',cart_product_id__product_brand_id__brand_name='Nike').values('cart_item_user_id').aggregate(count_of_customer=Count('cart_item_user_id'))
    # {'count_of_customer': 6}
    
    # 6. get the customer details(email and phone number) who didn't place any order in this month(march)
    cust_notPlaced_march=Customers.objects.exclude(customer_id__in=Placed_orders.objects.filter(placed_order_date__month='03').values('placed_order_user_id').distinct()).values_list('customer_email','customer_phone')
    # <QuerySet [('michael@gmail.com', '8555599999'), ('pragathi@gmail.com', '5888812345')]>
    
    # 7. most purchased item in march
    most_purchase_march=Cart.objects.filter(cart_item_placed_id__placed_order_date__month='03').values('cart_item_name').annotate(purchase_count=Count('cart_item_id')).order_by('-purchase_count')[:1]
    # <QuerySet [{'cart_item_name': 'Track Suit','purchase_count': 3}]>

    # 8. did user ordered Dell laptop and Raymond shirt in march?
    apple_laptop_march=Cart.objects.filter(cart_product_id__product_name='laptop',cart_product_id__product_brand_id__brand_name='Dell',cart_item_placed_id__placed_order_date__month='03').values('cart_product_id__product_brand_id__brand_name','cart_product_id__product_name').annotate(count=Count('cart_item_id'))
    # <QuerySet [{'cart_product_id__product_brand_id__brand_name': 'Dell', 'cart_product_id__product_name': 'Laptop', 'count': 2}]>
    raymond_shirt_march=Cart.objects.filter(cart_product_id__product_name='Shirt',cart_product_id__product_brand_id__brand_name='Raymond',cart_item_placed_id__placed_order_date__month='03').values('cart_product_id__product_brand_id__brand_name','cart_product_id__product_name').annotate(count=Count('cart_item_id'))
    # <QuerySet [{'cart_product_id__product_brand_id__brand_name': 'Raymond', 'cart_product_id__product_name': 'Shirt', 'count': 2}]>
    
    return render(request,'task2.html')