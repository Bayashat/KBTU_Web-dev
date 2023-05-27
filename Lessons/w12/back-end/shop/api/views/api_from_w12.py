import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from api.models import Product, Category
from api.serializers import CategorySerializer, ProductSerializer

@csrf_exempt
def category_list(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        # The task for serializer is take each object from array and extract 'id' and 'name', then will be converted to dict and returned

        # serializer = CategorySerializer1(categories, many=True)  # When we are providing list of objects, we need to set many=True
        serializer = CategorySerializer(categories, many=True)  # When we are providing list of objects, we need to set many=True
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)  # here we are returning only 1 object, so don't need safe=False
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def category_detail(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, status=404)

    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        serializer = CategorySerializer(instance=category, data=json.loads(request.body))
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        category.delete()
        return JsonResponse({'deleted': True}, status=204)


@csrf_exempt
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)


@csrf_exempt
def product_detail(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, status=404)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = json.loads(request.body)
        serilizer = ProductSerializer(instance=product, data=data)
        if serilizer.is_valid():
            serilizer.save()
            return JsonResponse(serilizer.data)
        return JsonResponse(serilizer.errors)

    elif request.method == 'DELETE':
        product.delete()
        return JsonResponse({'deleted': True}, status=204)
