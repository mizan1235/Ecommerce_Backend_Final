# Generated by Django 4.2.3 on 2024-03-03 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce', '0006_card'),
    ]

    operations = [
        migrations.CreateModel(
            name='orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('mobile', models.CharField(max_length=14)),
                ('pin', models.IntegerField()),
                ('address', models.CharField(max_length=150)),
                ('flat_no', models.CharField(max_length=10)),
                ('state', models.CharField(max_length=20)),
            ],
        ),
    ]