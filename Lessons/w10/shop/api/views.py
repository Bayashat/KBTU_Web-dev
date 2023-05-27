from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import Product


# Create your views here.
def product_list(request):
    products = Product.objects.all()  # select * from api_product;
    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json, safe=False)

    # product_list = list(products.values())
    # return JsonResponse(product_list, safe=False)


def product_detail(request, product_id):
    try:
        product = Product.objects.get(id=product_id)  # SELECT * FROM api_products WHERE id = <product_id>;
    except Product.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse(product.to_json())
