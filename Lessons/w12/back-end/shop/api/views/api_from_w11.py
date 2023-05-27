import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from api.models import Product, Category


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
            return JsonResponse({'error': str(e)}, status=404)
        # product = Product.objects.create(name=data['name'], price=data['price'], description=data['description'],
        #                                  category=category)
        product = Product.objects.create(**data, category=category)
        return JsonResponse(product.to_json())


@csrf_exempt
def product_detail(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, status=400)

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
