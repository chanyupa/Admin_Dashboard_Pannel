from django.db import models

# Create your models here.
class Data_Entry_Pannel(models.Model):
    bookingcode = models.CharField(max_length=100)
    passengername = models.CharField(max_length=100)
    prize = models.CharField(max_length=100)
    issueby = models.CharField(max_length=100)
    eticketnumber = models.CharField(max_length=100)
    passportnumber = models.CharField(max_length=100)
    ticketfees = models.CharField(max_length=100)

class Customer_Table(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    createdat = models.CharField(max_length=100)

class Banner_Table(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    createdat = models.CharField(max_length=100)
    updatedat = models.CharField(max_length=100)

class Payment_Table(models.Model):
    id = models.IntegerField(primary_key=True)
    paymenttype = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=100)
    createdat = models.CharField(max_length=100)

class Delifee_Table(models.Model):
    id = models.IntegerField(primary_key=True)
    regionname = models.CharField(max_length=100)
    township = models.CharField(max_length=100)
    deliveryfees = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    createdat = models.CharField(max_length=100)
    updatedat = models.CharField(max_length=100)

class Region_table(models.Model):
    id = models.IntegerField(primary_key=True)
    regionname = models.CharField(max_length=100)
    createdat = models.CharField(max_length=100)
    updatedat = models.CharField(max_length=100)

class Product_Table(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    stock = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    unit = models.CharField(max_length=100)
    createdat = models.CharField(max_length=100)

class Information_Table(models.Model):
    id = models.IntegerField(primary_key=True)
    content = models.CharField(max_length=100)
    createdat = models.CharField(max_length=100)
    updatedat = models.CharField(max_length=100)

class Category_Table(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    createdat = models.CharField(max_length=100)
    updatedat = models.CharField(max_length=100)

class Brand_Table(models.Model):
    id = models.IntegerField(primary_key=True)
    categoryname = models.CharField(max_length=100)
    brandname = models.CharField(max_length=100)
    createdat = models.CharField(max_length=100)
    updatedat = models.CharField(max_length=100)

class Order_table(models.Model):
    orderid = models.IntegerField(primary_key=True)
    customer = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    updatedat = models.CharField(max_length=100)
    orderdate = models.CharField(max_length=100)
