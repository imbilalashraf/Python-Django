from django.db import models

class Car(models.Model):
    car_name = models.CharField(max_length=100) 
    car_model = models.IntegerField()  
    car_speed = models.IntegerField()  
