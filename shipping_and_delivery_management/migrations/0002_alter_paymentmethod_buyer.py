# Generated by Django 5.1.1 on 2024-10-04 21:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipping_and_delivery_management', '0001_initial'),
        ('user_management', '0003_buyer_payment_methods_user_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentmethod',
            name='buyer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='all_payment_methods', to='user_management.buyer'),
        ),
    ]
