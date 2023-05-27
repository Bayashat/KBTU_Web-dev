#   Week - 12
## DRF Serialization
* Creating a Serializer classes
* Working with Serializers
* Types of Serializer classes
* Simple Serializer classes
* Model Serializers
* Writing regular Django views using our Serializer

## Laboratory Work - 10: https://docs.google.com/document/d/1Uqa9ok5U-q21Yu7TN6H5eiPPjYibPFmQ5lPA5hMpWpE/edit?usp=sharing

### 1. Connect Frontend(Angular side) with Backend(Django side)
```bash
1. Create a new Angular project and use previoud django project as backend
2.0 For Back-End side: 
2.1 install "pip install django-cors-headers" and add "corsheaders" to INSTALLED_APPS in settings.py in Django part. This will allow us to make requests from our Angular frontend to our Django backend
2.2 add "corsheaders.middleware.CorsMiddleware" to MIDDLEWARE in settings.py in Django part
2.3 add "CORS_ORIGIN_ALLOW_ALL = True" to settings.py or 
    "CORS_ALLOWED_ORIGINS = [
        "http://localhost:4200",
    ]" to settings.py in Django part     This means we are listing which origins are allowed to make requests to our Django server
3.0 For Front-End side:
3.1 Write HTML page using Category interface to display all categories
3.2 Using HttpClientModule and Angular Service to send requests to Django server("http://127.0.0.1:8000")
```

### 2. Django REST Framework(DRF), Serializers
```bash
0. We shouldn't write to_json method in our models.py file, because we have serializers
1.1 Install Django REST Framework(DRF) using "pip install djangorestframework"
1.2 Add "rest_framework" to INSTALLED_APPS in settings.py in Django part
2.1 Create folder "views", inside it create different view files for use
2.2 You can do it for models also, create seperate folder for models, it's not good to put all models in one models.py file
3.1 Created serializers.py file in Django part, and wrote 2 types of serializers: Simple Serializer and Model Serializer
3.2 Simple Serializer is used when we want to serialize data that is not directly related to a model, Model Serializer is used when we want to serialize data that is directly related to a model
4.0 We used serializers in api_from_w12.py file with FBV(Modified from w11)
4.1 When  using serializer handling 'GET' request, we should provide 'queryset' and 'many=True' arguments to serializer
4.2 When handling 'POST' request, we should provide 'data=json.loads(request.body)' argument to serializer
4.3 When handling 'PUT' request, we should provide 'instance=category' and 'data=json.loads(reqeust.body)' arguments to serializer
```

