# Generated by Django 4.1.7 on 2023-06-26 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0028_rename_product_cartitem_name_cartitem_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='quan',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
