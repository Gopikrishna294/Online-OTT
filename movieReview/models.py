from django.db import models

# Create your models here.
class Movie(models.Model):
    food_Id = models.AutoField(primary_key=True)
    food_Name = models.CharField(max_length=50)
    food_Price = models.FloatField()