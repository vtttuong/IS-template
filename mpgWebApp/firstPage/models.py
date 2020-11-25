from django.db import models

# Create your models here.
class Match(models.Model):
    series = models.CharField(max_length=50)
    season = models.IntegerField()
    round = models.IntegerField()
    homename = models.CharField(max_length=50)
    homelogo = models.CharField(max_length=500)
    homegoals = models.CharField(max_length=50)
    awayname = models.CharField(max_length=50)
    awaylogo = models.CharField(max_length=500)
    awaygoals = models.IntegerField()
    stadiumname = models.CharField(max_length=100)
    startdate = models.CharField(max_length=50)