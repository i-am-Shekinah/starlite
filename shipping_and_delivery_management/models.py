from django.db import models

class ShippingAddress(models.Model):
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.address_line_1}, {self.city}, {self.country}'
    
class PaymentMethod(models.Model):
    PAYMENT_CHOICES = (
        ('paypal', 'Paypal'),
        ('credit_card', 'Credit Card'),
        ('bank_transfer', 'Bank Transfer'),
    )
    buyer = models.ForeignKey('user_management.Buyer', on_delete=models.CASCADE, related_name='all_payment_methods')
    payment_type = models.CharField(max_length=50, choices=PAYMENT_CHOICES)
    provider_name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=50)
    expiry_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.payment_type}, {self.buyer.user.username}'