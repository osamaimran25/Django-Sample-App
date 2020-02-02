from django.db import models

# Create your models here.


class Owner(models.Model):
    id              = models.AutoField(primary_key=True)
    name            = models.CharField(max_length=255)
    password        = models.CharField(max_length=255)

class Cat(models.Model):
    id              = models.AutoField(primary_key=True)
    name            = models.CharField(max_length=255)
    date_of_birth   = models.DateField()
    owner           = models.ForeignKey(Owner, on_delete=models.CASCADE)


class Dog(models.Model):
    
    id              = models.AutoField(primary_key=True)
    name            = models.CharField(max_length=255)
    date_of_birth   = models.DateField()
    owner           = models.ForeignKey(Owner, on_delete=models.CASCADE)
