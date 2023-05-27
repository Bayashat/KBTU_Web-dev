from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from api.models import Category, Product
from api.serializers import CategorySerializer, ProductSerializer, CategorySerializer2


class CategoryListAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer2
    permission_classes = (IsAuthenticated, )
    # permission_classes = (AllowAny, )

    # def get_queryset(self):  # Filtering the queryset based on the user
        # return Category.objects.filter(user=self.request.user)

    # def perform_create(self, serializer):  # in this process we can identify the user who created the object
    #     serializer.save(user=self.request.user)


class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer2
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class ProductListAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

