from django.urls import path
from api.views import *

from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('login/', obtain_jwt_token),  #  obtaining a token via a POST included the user's username and password

    # For FBV
    # path('categories/', category_list),
    # path('categories/<int:category_id>/', category_detail),
    #
    # path('products/', product_list),
    # path('products/<int:product_id>/', product_detail),

    # For CBV
    # path('categories/', CategoryListAPIView.as_view()),
    # path('categories/<int:pk>/', CategoryDetailAPIView.as_view()),
    #
    # path('products/', ProductListAPIView.as_view()),
    # path('products/<int:pk>/', ProductDetailAPIView.as_view()),

    # For Generic Views
    path('categories/', CategoryListAPIView.as_view()),
    path('categories/<int:pk>/', CategoryDetailAPIView.as_view()),

    path('products/', ProductListAPIView.as_view()),
    path('products/<int:pk>/', ProductDetailAPIView.as_view()),
]