#import resource
from django.db import models
from tastypie.resources import ModelResource
from movies.models import Movie
# Create your models here.
# Restful api
# Representational state transfer


class MovieResource(ModelResource):
    class Meta:
        queryset = Movie.objects.all()  # simply retunrs a query. Lazy loading
        resource_name = 'movies'
        excludes = ['date_created']
