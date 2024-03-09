from django.db import models

# Create your models here.
class product_details(models.Model):
    seller_email=models.EmailField(max_length=40,blank=False,default='rohan@gmail.com')
    title=models.CharField(max_length=200,blank=False)
    price=models.IntegerField()
    category=models.CharField(max_length=40,blank=False)
    desc=models.TextField(blank=False)
    image= models.FileField(upload_to='Products/',max_length=250,null=True,default=None)


class user_details(models.Model):
    name=models.CharField(max_length=40)
    email=models.EmailField(primary_key=True)
    phone=models.CharField(max_length=10)
    password=models.CharField(max_length=100)

class card(models.Model):
    email=models.EmailField(max_length=30)
    product_id=models.IntegerField()

class orders(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=25)
    mobile=models.CharField(max_length=14)
    pin=models.IntegerField()
    address=models.CharField(max_length=150)
    flat_no=models.CharField(max_length=10)
    state=models.CharField(max_length=20),
    date=models.CharField(max_length=15,default='1/3/2024')
