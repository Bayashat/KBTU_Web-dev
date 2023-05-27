#   Week - 11
## Generic Views, Sessions, Users, and Registration
* Using Generic Views
* Generic Views of Objects
* Django’s Session Framework
* Users and Authentication

## Laboratory Work - 9: https://docs.google.com/document/d/1NPrFcySi36t12v70SY2IPzIbVpnXmh4Z_6COf_b6R8M/edit?usp=sharing

### 1. Initial Setup:
```bash
1. 将上周的项目复制到本周的文件夹中. 并进行调整
2.1 这周我们将使用 Postman 工具来测试我们的 API (用于发送 HTTP 请求: GET, POST, PUT, DELETE)
2.2 在 Postman 的 Collections 中创建一个新的 Collection, 并将其命名为 "WebDev2023". 在里面添加文件夹叫 "W11". 在里面创建相应的请求
2.3 在 Postman 的 Environments 中创建一个新的 Environment, 并将其命名为 "DEV SERVER". 在里面添加变量 "BASE_URL" 并将其值设置为 "http://localhost:8000". 以便我们可以在请求中使用 {{BASE_URL}} 来代替 "http://localhost:8000"
```

### 2. Django Shell:
```bash
1. 进入项目的根目录后, 通过 "python manage.py shell" 命令来进入 Django Shell. 
2. 通过它我们可以在 Python 环境中执行 Django 代码. 也可以执行数据库操作(增删改查)
```

### 3. Table Relationships:
```bash
1. 在 Django 中, 通过 ForeignKey 来建立表与表之间的关系. 例如: 一个Category可以有多个Product, 但是一个Product只能属于一个Category. 
2. 我们在 models 里创建了 Category 表(字段: name)
3. 并在 Product 表中添加一个 category 字段, 并将其设置为 ForeignKey: category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products')
4. 在数据库, Django会自动为 ForeignKey 字段添加 "_id" 后缀. 例如: category_id
4. 添加 class Meta: verbose_name 与 verbose_name_plural 来设置表的显示名称
4. 通过 "python manage.py makemigrations" 和 "python manage.py migrate" 命令来创建和执行数据库迁移. 
5. 在 admin.py 中使用 @admin.register(table_name) 来注册 Category 表 和 Product 表, 并指定显示的字段
```

### 4. CRUD Operations:
```bash
1. 在 views.py 中对同一个url, 通过不同的请求方法来执行不同的操作. 例如: GET, POST, PUT, DELETE
2. 注意: 在需要使用POST请求的视图函数, 通过 "from django.views.decorators.csrf import csrf_exempt" 并使用@csrf_exempt来取消 csrf 验证
```
