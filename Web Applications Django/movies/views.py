from django.http import HttpResponse, Http404

from django.shortcuts import render, get_object_or_404

from .models import Movie

# Create your views here.


def index(request):
    movies = Movie.objects.all()
    #output = ', '.join([m.title for m in movies])
    # SELECT * FROM movies_movies
    # Movie.objects.filter(release_year=1984)
    # SELECT * FROM movies_movie WHERE  release_year=1984
    # Single object
    # Movie.objects.get(id=1)
   # return HttpResponse(output)
    return render(request, 'movies/index.html', {'movies': movies})

    # For each movie added we want to render a table row
    # We use double curly and django also has powerful code snppets

    # As best practice we do not want a generic name index.html. We create a namespace movies inside templates folder of app movies and move index.html inside


def detail(request, movie_id):

    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})
