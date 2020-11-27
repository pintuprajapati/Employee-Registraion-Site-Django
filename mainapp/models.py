from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField
from django import forms

# Create your models here.
class Employee(models.Model):
    
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    emp_id = models.IntegerField()
    email_id = models.CharField(max_length=200)
    address = models.TextField(max_length=500)
    city = models.CharField(max_length=200)
    mobile = models.IntegerField()
    # birthday = models.CharField(max_length=200)
    birthday = models.DateField()
    

    ## Dunder method
    def __str__(self):
        return self.firstname