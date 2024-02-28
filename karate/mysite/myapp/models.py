from django.db import models
from django_jalali.db import models as jmodels

      

class Account(models.Model):
    name=models.CharField(max_length=250)
    email=models.EmailField()
    password=models.CharField(max_length=250)

    def __str__(self):
        return self.name
    
    

class Gym(models.Model):
    objects=jmodels.jManager()
    coach_name=models.CharField(max_length=250)
    time=jmodels.jDateField()
    location=models.CharField(max_length=200)
    level=models.CharField(max_length=200)
    coach_level=models.CharField(max_length=200)
    price=models.FloatField()

    
    def __str__(self):
        return self.coach_name
    
