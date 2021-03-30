from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Certificate(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE,null=True)
    eureka_jr = models.ImageField(upload_to='ecell_certificate',max_length=100,blank=True,null=True)
    workshop = models.ImageField(upload_to='ecell_certificate',max_length=100,blank=True,null=True)
    bootcamp = models.ImageField(upload_to='ecell_certificate',max_length=100,blank=True,null=True)

    def __str__(self):
        return self.user.username