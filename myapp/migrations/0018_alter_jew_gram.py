# Generated by Django 4.1.7 on 2023-04-18 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_alter_jew_gram'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jew',
            name='gram',
            field=models.IntegerField(null=True),
        ),
    ]
