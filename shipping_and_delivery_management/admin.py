from django.contrib import admin
from .models import ShippingAddress, PaymentMethod

admin.site.register(ShippingAddress)
admin.site.register(PaymentMethod)