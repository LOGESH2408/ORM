from django.db import models
from django.contrib import admin
class Product(models.Model):
    ProductID=models.CharField(primary_key=True,max_length=7)
    Name=models.CharField(max_length=30)
    Quantity=models.IntegerField()
    Model=models.CharField(max_length=10)
    Date_of_Manufacture=models.DateTimeField()
    Reviews=models.IntegerField()
    Colour=models.CharField(max_length=30)
class ProductAdmin(admin.ModelAdmin):
    list_display=["ProductID","Name","Quantity","Model","Date_of_Manufacture","Reviews","Colour"]
