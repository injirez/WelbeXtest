from django.db import models

class Main(models.Model):
    date = models.DateTimeField()
    title = models.CharField(max_length=15)
    quantity = models.IntegerField()
    distance = models.IntegerField()
