from django.db import models

# Create your models here.
class UserDetails(models.Model):
    username=models.CharField(max_length=10)
    email=models.EmailField()
    pinCode=models.CharField(max_length=6,default="00000",blank=True)
    state=models.CharField(max_length=30,default="",blank=True)
    district=models.CharField(max_length=30,default="",blank=True)

