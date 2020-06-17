from django.db import models

# Create your models here.
PRODUCT_CATEGORIES=(
    ('men','men'),
    ('women','women'),  
    ('kids','kids'),
)
PRODUCT_NAME=(
    ('tshirrt','tshirt'),
    ('shirt','shirt'),
    ('pant','pant'),
)
class Product(models.Model):
    product_name=models.CharField(max_length=20,choices=PRODUCT_NAME,blank=True)
    product_price = models.CharField(max_length=20,blank=True)
    website_Image1=models.FileField(blank=True,)
    product_cate=models.CharField(max_length=10,choices=PRODUCT_CATEGORIES,blank=True)
    Description=models.TextField(max_length=6000,blank=True)

    def __str__(self):
        return self.product_name+" "+self.product_price
class Order(models.Model):
    Order_code=models.CharField(max_length=255,blank=True)
    User_fk = models.CharField(max_length=255, blank=True)
    Product_fk = models.CharField(max_length=255, blank=True)
    Order_date = models.CharField(max_length=255, blank=True)
    Order_total = models.CharField(max_length=255, blank=True)
    Order_status = models.CharField(max_length=255, blank=True)
    Order_Del = models.CharField(max_length=255, blank=True)

class Registration(models.Model):
    Username=models.CharField(max_length=200)
    Password = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)