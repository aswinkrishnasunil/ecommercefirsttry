# Generated by Django 4.1.7 on 2023-04-11 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_staf_add'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enq',
            name='message',
        ),
        migrations.AddField(
            model_name='enq',
            name='password',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
