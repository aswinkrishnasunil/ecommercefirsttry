# Generated by Django 4.1.7 on 2023-06-24 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0026_remove_cart_users'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='cart',
            new_name='cartitem',
        ),
    ]
