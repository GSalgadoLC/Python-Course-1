from django.urls import path
from . import views

# movies/
# movies/1/details

urlpatterns = [
    # path("") represents index page, we need to map to a view function. So we need to import views from the movies directory not the vidly directory
    # views.index is simplay calling it as a reference
    path('', views.index, name='index')

]

# We refer to the entire urlpatterns block as the url configuration

# As is our django application is not aware of the movies app we need to add a new path object in the urlpattern of vidly directory
