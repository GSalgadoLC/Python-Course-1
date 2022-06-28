from django.http import HttpResponse

from django.shortcuts import render

from .models import Movie

# Create your views here.


def index(request):
    movies = Movie.objects.all()
    output = ', '.join([m.title for m in movies])
    # SELECT * FROM movies_movies
    # Movie.objects.filter(release_year=1984)
    # SELECT * FROM movies_movie WHERE  release_year=1984
    # Single object
    # Movie.objects.get(id=1)
    return HttpResponse(output)
