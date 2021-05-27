from django.db import models
from django.db.models.deletion import CASCADE

class dojo(models.Model):
    name=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    state=models.CharField(max_length=255)

class ninjas(models.Model) :
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    dojo=models.ForeignKey(dojo,related_name='ninja',on_delete=CASCADE)

# Create your models here.
