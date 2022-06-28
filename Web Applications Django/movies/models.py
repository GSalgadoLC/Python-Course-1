from django.db import models
from django.utils import timezone

# Create your models here.


class Genre(models.Model):
    # Django will automatically store genre objects in a data base
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    number_in_stock = models.IntegerField()
    daily_rate = models.FloatField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)

# We are simly applying a reference not calling it because then the current datetime would be hardcoded
