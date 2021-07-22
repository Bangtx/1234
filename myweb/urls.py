from django.contrib import admin
from django.urls import path
from . views import myweb


urlpatterns = [
    path('test/', myweb().test, name='test'),
    path('', myweb().index, name='index'),
    path('product/<int:id>', myweb().product, name='product'),
    path('productdetails/<int:id>', myweb().product_details, name='product-details')
]
