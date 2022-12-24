from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.


company_chooses = (
    ("Company","Company"),
    ("Trader","Trader"),
    ("Wholeseller","Wholeseller"),
    ("Broker","Broker"),
    ("Other","Other"),
)

class Person_information(models.Model):
    Name_of_supplier = models.CharField(max_length=50,null=True,blank=True)
    contact_number = models.IntegerField(null=True,blank=True)
    Email = models.EmailField(null=True,blank=True)
    Name_of_his_company = models.CharField(max_length=100,null=True,blank=True)
    Type_of_organization = models.CharField(max_length=50,choices=company_chooses,default="Company")
    gst_number = models.TextField(blank=True,null=True)
    # industry_type = models.CharField(max_length=100,blank=True,null=True)
    def __str__(self):
        return self.Name_of_supplier

class order(models.Model):
    M_name = models.CharField(max_length=100,null=True,blank=True)
    M_price = models.IntegerField(null=True,blank=True)
    M_quantity = models.IntegerField(null=True,blank=True)
    M_saller = models.CharField(max_length=50,null=True,blank=True)
    M_comapany = models.CharField(max_length=100)
    M_amount = models.FloatField(blank=True,null=True)
    M_date = models.DateField(default=datetime.now(),blank=True,null=True)
    customer_name = models.CharField(max_length=50,blank=True,null=True)


class Instock(models.Model):
    product_name = models.CharField(max_length=100,null=True,blank=True)
    product_price = models.IntegerField(null=True,blank=True)
    product_quantity = models.IntegerField(null=True,blank=True)
    product_total_amount = models.FloatField(null=True,blank=True)
    N_supplier_name = models.ForeignKey(Person_information,on_delete=models.CASCADE)
    Product_company_name = models.CharField(max_length=50,blank=True,null=True)
    Receiver_name = models.CharField(max_length=50,blank=True,null=True)
    bill_number = models.IntegerField(blank=True,null=True)
    product_data = models.DateTimeField(default=datetime.now(),blank=True,null=True)

