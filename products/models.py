from django.db import models

class Product(models.Model):
    type_of_product=(
        ('Cosmetics','Cosmetics'),
        ('Mylomoika','Mylomoika')
    )

    name= models.CharField(max_length=50)
    image=models.ImageField(blank=True,null=True,default='default_product_image.jpg')
    description=models.TextField()
    type=models.CharField(choices=type_of_product,max_length=200)
    price=models.CharField(max_length=50)

    def __str__ (self):
        return f"{self.name},{self.type},{self.price}"


class Order(models.Model):
    statuses=(
        ('In Process','In Process'),
        ('Delivered','Delivered'),
        ('Not Delivered','Not Delivered',)
)
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    quantity=models.IntegerField(default=1)
    status=models.CharField(max_length=20,choices=statuses,default='In Process')
    date_created=models.DateTimeField(auto_now_add=True)

class AboutUs(models.Model):
    title=models.CharField(max_length=150)
    description=models.TextField()





# Create your models here.
