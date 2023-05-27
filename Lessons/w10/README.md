#   Week - 10
## Building REST APIs With Django REST Framework:
* Fundamentals of Basic REST API Design
* REST API Architecture
    * Grouping API URLs
    * Version Your API

## Laboratory Work - 8: https://docs.google.com/document/d/1ZDK6MbLP1eQrGC5gMkxVCoZ75dbbGdW34l9TwgnLer4/edit?usp=sharing


### 1. Initial Setup:
```bash
1. Create a new Django project called "shop" using the django-admin command 
2. Create a new Django app called "api" using the manage.py command
```

### 2. URLs conf
```bash
1. 在项目根目录下的urls.py中写了几种url的匹配方式(包括path 和 re_path(正则表达式))
2. 创建了一个api的url，用于匹配api的url
```

### 3. Django Applications, REST API, and JSON 
```bash
0. 使用 "python manage.py startapp main" 命令创建了一个名为 main 的app
1. Django项目是由多个app组成的，每个app都是一个独立的模块，可以被其他的项目所使用(类似前端框架的组件)
2. 在项目根目录下的settings.py中的INSTALLED_APPS中添加了api这个app
3. 在 shop/urls.py 中通过 include() 函数将 main.urls 包含进来. 
4. 在 main/urls.py 中添加了数个路由, 用于匹配不同的请求. 
5. 在 main/views.py 中添加了数个函数, 用于处理不同的请求. 并通过基本的函数返回了一些数据(JsonResponse). 通过本地创建数据的方式, 模拟了数据库的查询操作.
```

### 4. Work with Django Models 
```bash
1. 创建了一个名为 api 的app. 并在 settings.py 中添加了 api 这个 app.
2.1 在 api/models.py 中创建了一个名为 Product 的模型. 并添加了一些字段.
2.2 给模型添加了 __str__ 魔法函数, 用于在 admin 界面中显示更加友好的字段名.
3.1 通过 "py manage.py makemigrations" 命令创建一个名为 0001_initial.py 的迁移文件. 并通过 "py manage.py migrate" 命令将模型同步到数据库中.
3.2 通过 "py manage.py showmigrations" 命令查看迁移文件的状态(which is applied or not).
3.3 之后就可以在数据库中看到新创建的表了
4.1 在 api/urls.py 中创建了两个路由, 用于匹配不同的请求.
4.2 在 api/views.py 中创建了一个名为 Product_list 的类, 用于处理 GET 请求. 并通过 Product.objects.all() 获取了数据库中的所有数据. 之后通过model里我们自写的 to_json 函数将数据转换成了 json 格式. 最后通过 JsonResponse 将数据返回给前端.
4.3 并创建了一个名为 Product_detail 的类, 用于处理 GET 请求. 并通过 Product.objects.get() 获取了数据库中的指定数据. 之后通过model里我们自写的 to_json 函数将数据转换成了 json 格式. 最后通过 JsonResponse 将数据返回给前端. 注意: 由于有可能存在请求的数据不存在的情况, 所以我们需要对这种情况进行处理. 通过 try...except... 来捕获异常, 并返回相应的错误信息.
5.1 在 api/admin.py 中注册了 Product 模型(使用 admin.site.register() 函数 或者 @admin.register() 装饰器).
5.2 之后就可以在 admin 界面中看到新注册的模型并对其进行操作了.
```


