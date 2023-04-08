"""
Eshopper django ecommerce site developed by vernonthedev
This is the admin file to hold the information about models that are 
presented in the backend of the webapplication.

"""


from django.contrib import admin
from .models import *

# register/apply the following models into the django backend
admin.site.register(
    [Admin, Customer, Category, Product, Cart, CartProduct, Order, ProductImage])

