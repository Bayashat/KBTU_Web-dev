from rest_framework.views import APIView
from rest_framework.response import Response

from django.shortcuts import Http404
from rest_framework import status

from api.serializers import CategorySerializer, ProductSerializer
from api.models import Category, Product


class CategoryListAPIView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Category.objects.get(id=pk)
        except Category.DoesNotExist as e:
            raise Http404  # or return Response(str(e), status=status.HTTP_404_NOT_FOUND

    def get(self, request, pk=None):
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk=None):
        category = self.get_object(pk)
        serializer = CategorySerializer(instance=category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        category = self.get_object(pk)
        category.delete()
        return Response({'deleted': True}, status=status.HTTP_204_NO_CONTENT)


class ProductListAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(id=pk)
        except Product.DoesNotExist as e:
            raise Http404  # or return Response(str(e), status=status.HTTP_404_NOT_FOUND

    def get(self, request, pk=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(instance=product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        product = self.get_object(pk)
        product.delete()
        return Response({'deleted': True    }, status=status.HTTP_204_NO_CONTENT)

