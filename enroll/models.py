from django.db import models

# Create your models here.
class User(models.Model):
    celebrity=models.CharField(max_length=50)
    movie=models.CharField(max_length=50)
    imdb=models.FloatField()
    