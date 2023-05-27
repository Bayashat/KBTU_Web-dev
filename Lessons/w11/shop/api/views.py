import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from api.models import Product, Category

#                           1) Selecting  Objects
"""
products = Product.objects.all()     #   get all products in a queryset / SELECT * FROM products;
"""

#                           2) Creating Objects
"""
Product.objects.create(name='iphone', price=1000)
"""

#                           3) Updating Objects
"""
p1 = Product(name='product xxx', price=5000, ...)
p1.save()  #   insert product into database

p1.price = 6000
p1.save()  #   update product in database
"""

#                           4) Deleting objects
"""
c = Category.objects.get(id=1)
c.delete()  #   delete category with id=1
"""

#                           5) Python Shell operations
"""
p = Product.objects.get(id=4)
p.category_id   # 1
p.category      # <Category: Phones>
p.category.name      # 'Phones'
p.category.to_json()    # {'id': 1, 'name': 'Phones'}


#                   1) without related_name
c = Category.objects.get(pk=1)
c.product_set.all()     # all products of category c

#                   2) with related_name
c = Category.objects.get(pk=1)
c.products.all()        # all products of category c


#                  3) Add object with related table with 'add'
c1 = Category.objects.get(id=5)
c1              #   <Category: PCs>
c1.products.all()   #   <QuerySet []>

p1 = Product.objects.create(name='ROG', description='asd', price=2000)
p1              #   <Product: ROG - 2000>

c1.products.add(p1)

c1.products.all()   #   <QuerySet [<Product: ROG - 2000.00>]>

"""

#                           6) Filtering Data
"""
Product.objects.get(id=1)   #   get product with id=1
Product.objects.filter(price=1000)  #   get all products with price=1000  / SELECT * FROM products WHERE price=1000;
Product.objects.filter(price__gt=1000)  #   get all products with price > 1000
Product.objects.filter(price__lt=1000)  #   get all products with price < 1000
Product.objects.filter(price__gte=1000)  #   get all products with price >= 1000
Product.objects.filter(price__lte=1000)  #   get all products with price <= 1000
Product.objects.filter(price__in=[1000, 2000])  #   get all products with price in [1000, 2000]
Product.objects.filter(price__range=[1000, 2000])  #   get all products with price in [1000, 2000]
Product.objects.filter(name__contains='iphone')  #   get all products with name contains 'iphone'
Product.objects.filter(name__startswith='iphone')  #   get all products with name starts with 'iphone'
Product.objects.filter(name__endswith='iphone')  #   get all products with name ends with 'iphone'
Product.objects.filter(name__iexact='iphone')  #   get all products with name equals 'iphone' (case insensitive)
Product.objects.filter(name__exact='iphone')  #   get all products with name equals 'iphone' (case sensitive)
Product.objects.filter(name__icontains='iphone')  #   get all products with name contains 'iphone' (case insensitive)
Product.objects.filter(name__istartswith='iphone')  #   get all products with name starts with 'iphone' (case insensitive)
Product.objects.filter(name__iendswith='iphone')  #   get all products with name ends with 'iphone' (case insensitive)
Product.objects.filter(name__regex=r'^iphone')  #   get all products with name matches regex '^iphone'
Product.objects.filter(name__iregex=r'^iphone')  #   get all products with name matches regex '^iphone' (case insensitive)
Product.objects.filter(name__isnull=True)  #   get all products with name is null
Product.objects.filter(name__isnull=False)  #   get all products with name is not null
Product.objects.filter(name__in=['iphone', 'samsung'])  #   get all products with name in ['iphone', 'samsung']
Product.objects.filter(name__in=['iphone', 'samsung']).exclude(price=1000)  #   get all products with name in ['iphone', 'samsung'] and price != 1000
Product.objects.filter(name__in=['iphone', 'samsung']).exclude(price__in=[1000, 2000])  #   get all products with name in ['iphone', 'samsung'] and price not in [1000, 2000]
Product.objects.filter(name__in=['iphone', 'samsung']).exclude(price__range=[1000, 2000])  #   get all products with name in ['iphone', 'samsung'] and price not in [1000, 2000]
Product.objects.filter(name__in=['iphone', 'samsung']).exclude(price__gt=1000)  #   get all products with name in ['iphone', 'samsung'] and price <= 1000
Product.objects.filter(name__in=['iphone', 'samsung']).exclude(price__gte=1000)  #   get all products with name in ['iphone', 'samsung'] and price < 1000
Product.objects.filter(name__in=['iphone', 'samsung']).exclude(price__lt=1000)  #   get all products with name in ['iphone', 'samsung'] and price >= 1000
Product.objects.filter(name__in=['iphone', 'samsung']).exclude(price__lte=1000)  #   get all products with name in ['iphone', 'samsung'] and price > 1000
Product.objects.filter(name__in=['iphone', 'samsung']).exclude(price__lt=1000, price__gt=2000)  #   get all products with name in ['iphone', 'samsung'] and price < 1000 or price > 2000
Product.objects.filter(name__in=['iphone', 'samsung']).exclude(price__lt=1000).exclude(price__gt=2000)  #   get all products with name in ['iphone', 'samsung'] and price < 1000 or price > 2000
Product.objects.filter(name__in=['iphone', 'samsung']).exclude(price__lt=1000).exclude(price__gt=2000).exclude(price=1500)  #   get all products with name in ['iphone', 'samsung'] and price < 1000 or price > 2000 or price = 1500
"""

#                           7) Ordering Data
"""
p = Product.objects.all().order_by('name')   #   get all products ordered by name  /  SELECT * FROM products ORDER BY name;
p = Product.objects.all().order_by('-name')  #   get all products ordered by name desc
p = Product.objects.all().order_by('name', '-price')  #   get all products ordered by name asc and price desc
"""


#       CRUD - CREATE, READ, UPDATE, DELETE
@csrf_exempt
def category_list(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        categories_json = [category.to_json() for category in categories]
        return JsonResponse(categories_json, safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)
        try:
            category = Category.objects.create(name=data['name'])
        except Exception as e:
            return JsonResponse({'error': str(e)})
        
        return JsonResponse(category.to_json())


@csrf_exempt
def category_detail(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, status=404)

    if request.method == 'GET':
        return JsonResponse(category.to_json())

    elif request.method == 'PUT':
        data = json.loads(request.body)
        category.name = data.get('name', category.name)
        category.save()
        return JsonResponse(category.to_json())

    elif request.method == 'DELETE':
        category.delete()
        return JsonResponse({'deleted': True}, status=204)


@csrf_exempt
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        return JsonResponse([product.to_json() for product in products], safe=False)

        # product_list = list(products.values())
        # return JsonResponse(product_list, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        try:
            category = Category.objects.get(id=data['category_id'])
        except Category.DoesNotExist as e:
            return JsonResponse({'error': str(e)}, status=400)
        # product = Product.objects.create(name=data['name'], price=data['price'], description=data['description'],
        #                                  category=category)
        product = Product.objects.create(**data, category=category)
        return JsonResponse(product.to_json())


@csrf_exempt
def product_detail(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, status=404)

    if request.method == 'GET':
        return JsonResponse(product.to_json())

    elif request.method == 'PUT':
        data = json.loads(request.body)
        try:
            category = Category.objects.get(id=data['category_id'])
        except Category.DoesNotExist as e:
            return JsonResponse({'error': str(e)}, status=404)
        product.name = data['name']
        product.price = data['price']
        product.description = data['description']
        product.category = category
        product.save()
        return JsonResponse(product.to_json())

    elif request.method == 'DELETE':
        product.delete()
        return JsonResponse({'deleted': True}, status=204)
