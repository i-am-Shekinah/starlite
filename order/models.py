from django.db import models

class Order(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('canceled', 'Canceled'),
    )
    buyer = models.ForeignKey('user_management.Buyer', on_delete=models.CASCADE, related_name='orders')
    cart = models.OneToOneField('cart.Cart', on_delete=models.CASCADE)
    ordered_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, default='pending')
    shipping_address = models.TextField(default='')

    def __str__(self):
        return f'Order {self.id} by {self.user.username}'
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order_items' ,on_delete=models.CASCADE)
    product_name = models.OneToOneField('product_management.Product', on_delete=models.CASCADE)
    # product_price =
