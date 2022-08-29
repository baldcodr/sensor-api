from django.db import models

class Sensor(models.Model):
    name = models.CharField(max_length=200,unique=True)
    unit = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Data(models.Model):
    date = models.CharField(max_length=200)
    sensor = models.CharField(max_length=200)
    value = models.FloatField()

    def __str__(self):
        return self.sensor +"-" + self.date