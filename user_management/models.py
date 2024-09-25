from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from cart.models import Cart
from product_management.models import Product

class User(AbstractUser):
    ROLE_CHOICES = (
        ('buyer', 'Buyer'),
        ('seller', 'Seller'),
    )

    # handles conflict with django.auth.User.groups
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_groups',
        blank=True,
    )
    
    # handles conflict with django.auth.User.user_permissions 
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',
        blank=True,
    )

    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    role = models.CharField(max_length=6, choices=ROLE_CHOICES)

    def __str__(self):
        return self.username
    

class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    # wishlist = 

    def __str__(self):
        return f'Buyer: {self.user.username}'
    

class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    store_name = models.CharField(max_length=255)
    products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return f'Seller: {self.user.username}'