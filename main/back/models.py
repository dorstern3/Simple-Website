from django.db import models

# Create your models here.

class Subscribe(models.Model):
    first_name= models.CharField(max_length=12)
    last_name= models.CharField(max_length=12)
    email= models.CharField(max_length=36)
    phone= models.BigIntegerField()
    message= models.CharField(max_length=200)