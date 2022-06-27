from django.db import models

# Create your models here.


class Genre(models.Model):
    # Django will automatically store genre objects in a data base
    name = models.CharField(max_length=255)


class Movie(models.Movie):
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    number_in_stock = models.IntegerField()
    daily_rate = models.FloatField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
