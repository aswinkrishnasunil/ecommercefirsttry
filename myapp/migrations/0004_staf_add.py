# Generated by Django 4.1.7 on 2023-04-11 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_staf'),
    ]

    operations = [
        migrations.AddField(
            model_name='staf',
            name='add',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
