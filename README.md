<img src="https://github.com/deanhoperobertson/django-rest-api/blob/main/django-logo.png" width="200"/>

# django-rest-api
- Create an api using Django REST API Framework. More information found [here](https://www.django-rest-framework.org/).

## Install and Set Up Project
```
pip install django
pip install djangorestframework
django-admin startproject PROJECTNAME
```

Push migrations and Run server
```
python manage.py migrate
python manage.py runserver
```

Create app and profile
```
python manage.py startapp APP_NAME
python manage.py createsuperuser
```

Create database and push
```
python manage.py makemigrations
python manage.py migrate
```

## Install Postman API
- Download Postman api [here](https://www.postman.com/downloads/).
- Create a free account.
- Copy and paste 'http://localhost:8000/courses/' to test a GET request in order to test our api is returning a payload and working as expected.
