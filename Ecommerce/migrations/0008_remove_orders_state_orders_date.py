# Generated by Django 4.2.3 on 2024-03-05 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce', '0007_orders'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='state',
        ),
        migrations.AddField(
            model_name='orders',
            name='date',
            field=models.CharField(default='1/3/2024', max_length=15),
        ),
    ]
