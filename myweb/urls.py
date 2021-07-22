from django.contrib import admin
from django.urls import path
from . views import myweb


urlpatterns = [
    path('/test', myweb().test, name='test'),
]
