from django.db import models

# Create your models here.
class brand(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=1000)
    created_at=models.DateTimeField(auto_now_add=True)

def __str__(self):
       return self.name

class Category(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=1000)
    created_at=models.DateTimeField(auto_now_add=True)

def __str__(self):
       return self.name

class Product(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    quantity=models.IntegerField()
    description=models.CharField(max_length=1000)
    is_avaliable=models.BooleanField()
    size=models.CharField(max_length=50)
    rating=models.IntegerField()
    brand_id=models.ForeignKey(brand,on_delete=models.CASCADE)
    cat_id=models.ForeignKey(Category,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

def __str__(self):
        return self.name

class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    phone=models.IntegerField()
    message=models.CharField(max_length=50)

def __str__(self):
        return self.name

