# Generated by Django 4.1.7 on 2023-04-24 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0020_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='jew',
            name='mod',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
