from django.db import models
class authors(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    notes=models.TextField(default="notes")
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    

class book(models.Model):
    title=models.CharField(max_length=255)
    desc=models.TextField()
    bkat=models.ManyToManyField(authors,related_name='books')
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)



# Create your models here.
