from __future__ import unicode_literals
from django.db import models
from datetime import datetime

# Create your models here.
class User(models.Model):
    first_name=models.CharField(max_length=45)
    last_name=models.CharField(max_length=45)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=25)
    # default is needed because dob field was added after data was input
    # otherwise you only need () after DateField
    dob=models.DateField(default=datetime.today, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
