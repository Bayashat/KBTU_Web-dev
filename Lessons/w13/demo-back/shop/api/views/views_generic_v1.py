from rest_framework import generics
from rest_framework import mixins

from api.models import Category, Product
from api.serializers import CategorySerializer, ProductSerializer


class CategoryListAPIView(mixins.ListModelMixin,
                          mixins.CreateModelMixin,
                          generics.GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CategoryDetailAPIView(mixins.RetrieveModelMixin,  # for getting one object
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            generics.GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # lookup_url_kwarg  = 'category_id'  # if you want to use another field for lookup (instead of pk)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
