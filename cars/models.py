from datetime import datetime
from django.db import models

# Create your models here.

class Car(models.Model):

    year_choice = []

    for r in range(2000,(datetime.now().year+1)):
        year_choice.append((r,r))

    


    car_title = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField(('year'), choices = year_choice)
    price = models.IntegerField()
    description = models.TextField(max_length=500)
    car_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    fuel_type = models.CharField(max_length=100)

   