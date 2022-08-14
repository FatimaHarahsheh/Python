from django.db import models
from django.db.models.deletion import CASCADE

class Dojo(models.Model):
    name=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    state=models.CharField(max_length=255)
    desc=models.TextField(default='old dojo')
    

class Ninja(models.Model) :
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    dojo=models.ForeignKey(Dojo, related_name='ninjas',on_delete=CASCADE)



# Create your models here.
