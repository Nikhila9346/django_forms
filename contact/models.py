from django.db import models

# Create your models here.
class Contact(models.Model):
    fname = models.CharField(max_length=15)
    name = models.CharField(max_length=13)
    email = models.EmailField()
    message = models.TextField()
