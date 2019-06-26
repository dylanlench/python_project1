from django.db import models
from datetime import datetime

class Admin(models.Model):
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Order(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField(default=datetime.now)
    billing_address = models.CharField(max_length=255)
    total = models.IntegerField(default = 0)
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)