"""
    This is the models file for ecom app(seperate app under ecomproject)
    Eshopper Ecommerce Web Application
    Coded and maintained by Jotham Prince
"""

# neccessary imports
from distutils.command.upload import upload
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from django.forms import ImageField
from django.http import HttpResponse
import datetime


# The admin model 
class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="admins")
    mobile = models.CharField(max_length=20)

    # how its saved in the admin panel
    def __str__(self):
        return self.user.username

# The customer model 
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200, null=True, blank=True)
    joined_on = models.DateTimeField(auto_now_add=True)

    # how its saved
    def __str__(self):
        return self.full_name

# The category model
class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    # set how the names should appear/ be presented in the admin backend panel
    class Meta:
        db_table = 'categories'
        verbose_name_plural = 'Categories'

    # how the name is saved
    def __str__(self):
        return self.title

# The product model 
class Product(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="products")
    marked_price = models.PositiveIntegerField()
    selling_price = models.PositiveIntegerField()
    description = models.TextField()
    in_stock = models.CharField(max_length=200, default="Fully stocked")
    warranty = models.CharField(max_length=300, null=True, blank=True)
    return_policy = models.CharField(max_length=300, null=True, blank=True)
    view_count = models.PositiveIntegerField(default=0)

    # how its saved in the admin panel
    def __str__(self):
        return self.title
    

# The product image model
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="products/images/")
    # how its saved
    def __str__(self):
        return self.product.title

# The CART model
class Cart(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True, blank=True)
    total = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    # how the name is saved the django admin backend
    def __str__(self):
        return "Cart: " + str(self.id)

# The CARTproduct model
class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rate = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    subtotal = models.PositiveIntegerField()

    # how the string is saved in the django admin backend
    def __str__(self):
        return "Cart: " + str(self.cart.id) + " CartProduct: " + str(self.id)

# The list of available order statuses
ORDER_STATUS = (
    ("Order Received", "Order Received"),
    ("Order Processing", "Order Processing"),
    ("On the way", "On the way"),
    ("Order Completed", "Order Completed"),
    ("Order Canceled", "Order Canceled"),
)

# The list of available payment methods in the webapplication
METHOD = (
    ("Cash On Delivery", "Cash On Delivery"),

)

# The Order model
class Order(models.Model):
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    ordered_by = models.CharField(max_length=200)
    shipping_address = models.CharField(max_length=200)
    mobile = models.CharField(max_length=10)
    email = models.EmailField(null=True, blank=True)
    subtotal = models.PositiveIntegerField()
    discount = models.PositiveIntegerField()
    total = models.PositiveIntegerField()
    order_status = models.CharField(max_length=50, choices=ORDER_STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(
        max_length=20, choices=METHOD, default="Cash On Delivery")
    payment_completed = models.BooleanField(
        default=False, null=True, blank=True)

    # how the string/name is saved in the django backend
    def __str__(self):
        return f" Order:{str(self.id)} : {self.mobile} "

