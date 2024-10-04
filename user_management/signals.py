from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import User, Buyer, Seller
from cart.models import Cart


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    '''
    Automatically create a Buyer or Seller instance based on the role whenever a new User is created.
    '''
    if created:
        if instance.role == 'buyer':
            cart = Cart.objects.create()
            Buyer.objects.create(user=instance, cart=cart)
        elif instance.role == 'seller':
            Seller.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    '''
    Save the profile whenever the User instance is saved
    '''
    if instance.role == 'buyer':
        # check if the Buyer instance exists, otherwise create it.
        Buyer.objects.get_or_create(user=instance, defaults={'cart': Cart.objects.create()})
    elif instance.role == 'seller':
        Seller.objects.get_or_create(user=instance)