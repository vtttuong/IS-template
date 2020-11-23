from django.db import models

# Create your models here.
class Match(models.Model):
    round = models.IntegerField()
    awayname = models.CharField(max_length=50)
    awaygoals = models.IntegerField()
    homename = models.CharField(max_length=50)
    homegoals = models.CharField(max_length=50)
    stadiumname = models.CharField(max_length=100)
    startdate = models.CharField(max_length=50)
    starttime = models.CharField(max_length=50)
