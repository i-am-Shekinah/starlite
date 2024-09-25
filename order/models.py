from django.db import models

class Order(models.Model):
    user = models.ForeignKey('user_management.User', on_delete=models.CASCADE)
    cart = models.OneToOneField('cart.Cart', on_delete=models.CASCADE)
    ordered_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, default='pending')

    def __str__(self):
        return f'Order {self.id} by {self.user.username}'