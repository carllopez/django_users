#django-users
## 
**django-users** is a basic test application to showcase how quick and easy you can create powerfull web applications with django without **any** dependency.

##Pre-requisites
- python 2.7

##Installation
Preferrably, set up an isolated virtual environment to avoid polluting your main development environment, although it's not really needed. Follow these steps and you'll be ready:

- $ pip install django==1.9
- $ git@github.com:carllopez/django_users.git

## Running the app
You're ready to test drive the application. Since it ships with an already ready sqlite database, we won't need to install any db migrations or initial data, just run:

- $ python manage.py runserver

## Running the app tests
Basic tests have been added to the app, they can be easily run with:

- $ python manage.py tests users.tests



