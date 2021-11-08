from django.db import models

# Create your models here.

class Car(models.Model):
	#id = models.IntegerField(unique=True, db_column='ID')
    driver_name = models.CharField(max_length=50)
    number_plate = models.CharField(max_length=30)
    contact = models.CharField(max_length=10)
    class Meta:
        db_table = "Cars"