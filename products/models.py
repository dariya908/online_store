from django.contrib.auth.models import User
from django.db import models
from datetime import date


class Product(models.Model):
    type_of_product = (
        ('Cosmetics', 'Cosmetics'),
        ('Mylomoika', 'Mylomoika')
    )

    name = models.CharField(max_length=50)
    image = models.ImageField(blank=True, null=True, default='default_product_image.jpg')
    description = models.TextField()
    type = models.CharField(choices=type_of_product, max_length=200)
    price = models.IntegerField(max_length=50)
    sale = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name},{self.type},{self.price}"


class Order(models.Model):
    statuses = (
        ('In Process', 'In Process'),
        ('Delivered', 'Delivered'),
        ('Not Delivered', 'Not Delivered',)
    )
    p_methods=(
        ('money','money'),
        ('wallet','wallet')
    )

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1)
    status = models.CharField(max_length=20, choices=statuses, default='In Process')
    date_created = models.DateTimeField(auto_now_add=True)
    payment_method=models.CharField(max_length=20,choices=p_methods)


class AboutUs(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()


class Contakts(models.Model):
    type_of = (
        ('Email', 'Email'),
        ('Phone number', 'Phone number'),
    )
    name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20)
    phonenumber = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    phy_adress = models.CharField(max_length=20)
    type = models.CharField(max_length=20, choices=type_of, default=phonenumber)
    latitude = models.IntegerField(blank=True, null=True)
    longtitude = models.IntegerField(blank=True, null=True)


class Profile(models.Model):
    genders = (
        ('F', 'F'),
        ('M', 'M')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='avatardefault_92824.png', blank=True)
    full_name = models.CharField(max_length=50)
    gender = models.CharField(choices=genders, max_length=20)
    description = models.TextField()
    birthdate = models.DateField(default=date.today())
    twitter = models.CharField(max_length=100)
    wallet=models.PositiveIntegerField(default=0)
    order_count=models.PositiveIntegerField(default=0)
    sale_amount=models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.user}"

# Create your models here.
