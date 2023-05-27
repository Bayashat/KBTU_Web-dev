#   Week-9
## Introduction to Python PL, Django:
* Python programming language
* What is Django?
* Django project structure
* Django configurations file (settings.py)
* Django router file (urls.py)
* Django Web Server Gateway Interface (wsgi.py)

## Laboratory Work - 7: https://docs.google.com/document/d/1hUejqqYaFgvj9zAeZ2r9NtbiQKm5tRnXttV6Jk7nmlo/edit?usp=sharing


### 0. Installing 
```bash
1. pip for installing packages: pip install "package_name"
2. Download Python: https://www.python.org/downloads/ (as minimun 3.8)
3. Download Virtual Environment: pip install virtualenv
```

### 1. Virtual Environment
```bash
1.1 Create virtual environment: python -m venv "env_name" / virtualenv "env_name"
1.2 If you have multiple Python version: python3.11 -m venv "env_name" / virtualenv "env_name" -p python3.11 
2.1 Activate virtual environment: "env_name"/Scripts/activate
2.2 Deactivate virtual environment: Deactivate
3.1 To see all packages in a environment: "pip freeze" will show all packages. Use "pip freeze > requirements.txt" to save all packages in a file.
3.2 To install all packages from a file: "pip install -r requirements.txt"
```

### 2. Intro to Django
```bash
0. Install django after activated virtual environment: pip install django==3.2.18
1. Create django project: django-admin startproject "project_name"
2. Run django project: python manage.py runserver
3. Create django app: python manage.py startapp "app_name"
4. Create migrations: python manage.py makemigrations
5. Migrate migrations: python manage.py migrate
6. Create superuser: python manage.py createsuperuser
```

### 3. Urls and Views
```bash
1. URLs 是 Django 中的路由系统, 它将 URL 模式映射到视图函数. 
2. Views 是 Django 中的视图系统, 它将 HTTP 请求映射到响应.
3. 在项目根目录下的 urls.py 文件中, 我们可以看到 urlpatterns 列表, 它是一个 URL 模式列表, 其中包含了 Django 项目中所有的 URL 模式.
4. 每个 URL 模式都会映射到一个视图函数, 这个视图函数会处理这个 URL 模式对应的 HTTP 请求.
5. 在 Django 项目中, 每个 app 都有自己的 urls.py 文件, 这个文件中包含了这个 app 中所有的 URL 模式.
6. 在 根目录下的 urls.py 里使用 include() 函数来包含 app 中的 urls.py 文件.
7. 在 app 中的 urls.py 文件中, 使用 path() 函数来定义 URL 模式.
8. path() 函数接收三个参数, 分别是 route、view 和 kwargs, 其中 route 参数是一个 URL 模式, view 参数是一个视图函数, kwargs 参数是一个字典, 包含了这个 URL 模式的其他参数.
9. 在 app 中的 views.py 文件中, 我们可以在视图函数中, 使用 render() 函数来渲染一个模板. 