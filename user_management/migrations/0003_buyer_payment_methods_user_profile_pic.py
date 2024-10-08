# Generated by Django 5.1.1 on 2024-10-04 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0002_remove_buyer_cart_buyer_shipping_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyer',
            name='payment_methods',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics/'),
        ),
    ]
