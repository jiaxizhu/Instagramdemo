from django.contrib import admin
from django.urls import path, include
from Insta.views import HelloDjango

urlpatterns = [

    path('', HelloDjango.as_view(), name='home')
]