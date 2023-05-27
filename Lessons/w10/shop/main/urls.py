from django.urls import path, re_path
from .views import home, about, hours_ahead, product_list, product_detail

urlpatterns = [
    path('home/', home),
    path('about/', about),
    re_path(r'^time/plus/(\d{1,2})/$', hours_ahead),

    path('products/', product_list),
    path('products/<int:product_id>/', product_detail),
]
