from django.contrib import admin

from .models import Product
# Register your models here.

#       1. 最基本的注册模型的方式: admin.site.register(model, admin_class=None, **options)
# admin.site.register(Product)
# admin.site.register(Category)


#       2. Python 装饰器语法: 作用是将一个 ModelAdmin 类注册到一个特定的模型上
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')

