from django.urls import path, re_path
import re
from . import views

urlpatterns = [
    re_path(r'^(?P<neighborhood>[\w-]*)/(?P<city>[\w-]*)/(?P<state>[\w-]*)/descriptions', views.neighborhoodDescriptions, name='index'),
    re_path(r'^(?P<neighborhood>[\w-]*)/(?P<city>[\w-]*)/(?P<state>[\w-]*)/photos', views.neighborhoodPhotos, name='index'),
    path('neighborhoods/rankings', views.getStandardDev, name='index'),
    re_path(r'^(?P<city>[\w-]*)/(?P<state>[\w-]*)/latlong', views.getLatAndLong, name="index")
]
