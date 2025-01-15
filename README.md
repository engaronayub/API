# API
## Create a Django Project

- (add the rest_framework and app)
- (create urls under app)
 
```django-admin startproject djangoapi```
- add project under settings
- migrate 
```winpty python manage.py migrate```

check if everything was installed as expected//
- ```python manage.py runserver```

- create  your app //

```python manage.py startapp api```

- creating models 


-  Views are pages you want to see ..//
- Create Serializers 
- Make it live
- Test your basic API


- Test your code wi

``` [
    {
        "id": 1,
        "url": "http://localhost:8000/courses/1/",
        "name": "Pi pico",
        "language": "English",
        "price": "50$",
        "description": "IoT support Tariff test1",
        "instructor": "Aron Ayub"
    },
    {
        "id": 2,
        "url": "http://localhost:8000/courses/2/",
        "name": "LLMs",
        "language": "English",
        "price": "20$",
        "description": "Introduction to LLMs",
        "instructor": "Aron Ayub"
    }
] ```