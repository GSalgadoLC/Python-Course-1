from django.contrib import admin
from .models import Genre, Movie
# Register your models here.


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class MovieAdmin(admin.ModelAdmin):
   # fields = ('title', ) can specify what you want to show or you can use exclude certain field
    exclude = ('date_created', )
    list_display = ('title', 'number_in_stock', 'daily_rate', )


admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
