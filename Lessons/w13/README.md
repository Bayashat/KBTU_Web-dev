#   Week - 13
## DRF Requests and Responses:
* Request objects
* Response objects
* Status codes
* Wrapping API views
* Pulling it all together

## Authentication:
* Adding endpoints for our User models
* Adding required permissions to views
* Adding login to the Browsable API
* Authenticating with the API

## Project Work requirements: https://docs.google.com/document/d/1ZYmBvHlS1rBeCb-Sy-yGU0M_8D5oaqiwgB_PS5-J75E/edit?usp=sharing


### I. For Back-End side
#### 1. DRF Requests and Responses and Class Based Views(CBV):
```bash
0. Used previous project but rewrite views file
1.0 Create "fbv.py" file for working with function based views
1.1 Wrapping with @api_view() decorator(from rest_framework.decorators import api_view) 这个装饰器用于将函数视图转换为基于函数的API视图 
1.2 Using 'status codes' from rest_framework.status
1.2 When using @api_view decorator, we will use 'Response' object from rest_framework.response, and when we handing POST request, we will use 'request.data' 
2.0 Create "cbv.py" file for working with class based views
2.1 Used APIView class from rest_framework.views and used Status codes from rest_framework.status
2.2 Handling all requests by only providing 'queryset' and 'serializer' attributes
3.0 Generic class-based views and Mixins
3.1 in "views_generic_v1.py" file we used generic Views in simple way: extending from several mixins and generic views
3.2 in "views_generic_v2.py" file we used generic Views in more easy way: extending from "ListCreateAPIView" and "RetrieveUpdateDestroyAPIView" classes
4. in "serializers.py" file we showed nested serializer(how to get Category with its products)
```


#### 2. Authentication & Permissions:
```bash
0. 本课程我们使用 JWT(JSON Web Token) 进行身份验证
1.0 使用DRF JWT 链接: https://jpadilla.github.io/django-rest-framework-jwt/ 安装 DRF JWT: pip install djangorestframework-jwt 并配置 settings.py
1.1 在 url.py 中配置 JWT 认证: path('login/', obtain_jwt_token) 这会通过 POST 请求验证用户身份, 如果正确: 返回一个 token
1.2 使用 Postman 进行测试时, 通过 POST 请求填入 admin 用户名和密码, 如果验证成功, 返回一个 token, 复制此token, 将其在发送 HTTP request 时, 添加在 Headers 中, 如: Authorization: JWT <your_token>
1.3 简化上述步骤: 在 Login 请求的 tests栏, 填入: 
        var jsonData = JSON.parse(responseBody);
        postman.setEnvironmentVariable("token", jsonData.token);
    即可自动获取 token 并添加在 Environment 里. 当发送请求时, 在 Headers 中填入: Authorization: JWT {{token}}
2.1 在 models.py 中从 django.contrib.auth.models 导入 User, 并在 Category 中添加 user = models.ForeignKey(User, related_name='categories', on_delete=models.CASCADE)
2.2 在 views.py 中, 通过重写 get_queryset() 方法, 筛选出当前用户的 Category, 使得当前用户才能看到自己创建的 Category
2.3 We have 2 options to add current user to Category: 
    1. 在 views.py 中, 通过重写 perform_create() 方法, 将 request.user 添加到 Category 中的 user 字段中
    2. 在 serializers.py 中, 往 CategorySerializer 中添加 user = serializers.HiddenField(default=serializers.CurrentUserDefault())


```

### II. For Front-End side

#### 1. JWT Authentication from Angular:
```bash
0. 创建component: category, 创建 service: category, login
1.1. 创建变量 logged, 用于判断用户是否登录, 并在 app.component.html 中使用, 当 logged=False时, 用户要看到登录页面, 当 logged=True时, 用户要看到主页面
1.2 当用户在登录页面填入用户名和密码后, 点击登录按钮, 会触发 login() 方法, 在该方法中, 通过 loginService, 向后端发送 POST 请求, 并将用户名和密码作为参数传入, 验证成功后, 后端会返回一个 token
1.3 在 login() 方法中, 通过调用 subscribe() 方法, 获取后端返回的 token, 并将其存入 localStorage 中(.setitem('token', data.token)), 以便后续使用
1.4 但是现在有个问题是当页面刷新时,还是会显示登录页面, 所以我们需要在 ngOnInit() 方法中, 通过调用 localStorage.getItem('token') 方法, 获取 token, 根据 token 是否存在, 来判断用户是否登录
1.5 创建 logout按钮, 点击时会触发 logout() 方法, 在该方法中, 通过调用 localStorage.removeItem('token') 方法, 删除 token, 并将 logged 设置为 False, 以便用户看到登录页面
2.0 现在我们需要在发送请求时, 将 token 添加到 Headers 中, 以便后端验证用户身份, 所以我们要使用 Angular 的 Interceptor
2.1 Interceptor 是一个服务, 用于在发送请求时, 拦截请求, 并在请求中修改 Headers, 然后再发送请求, 类似于 Django 中的 Middleware
2.2 创建 auth.interceptor.ts 文件, 并在其中创建 AuthInterceptor 类, 该类继承 HttpInterceptor, 并重写 intercept() 方法, 在该方法中, 通过调用 localStorage.getItem('token') 方法, 获取 token, 并将其添加到 Headers 中, 最后返回 req
2.3 在 app.module.ts 中, 在 providers 中, 添加 {provide: HTTP_INTERCEPTORS, useClass: AuthInterceptor, multi: true}
2.4 现在, 当我们发送请求时, Interceptor 会自动将 token 添加到 Headers 中, 以便后端验证用户身份
```
