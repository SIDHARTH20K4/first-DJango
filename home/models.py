from django.db import models

# Create your models here.
class contact(models.Model):
    Email = models.CharField(max_length=122)
    Password = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)