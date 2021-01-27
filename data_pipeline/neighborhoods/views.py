from django.shortcuts import render
from django.http import HttpResponse
from .getNeighborhoodDescriptions import getDescriptions
from .getPlacePhotos import getPhotos
# Create your views here.

def neighborhoodDescriptions(request, neighborhood, city, state):
    description = getDescriptions(neighborhood, city, state)
    print(neighborhood, city, state)
    response = HttpResponse(description)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
    return response
def neighborhoodPhotos(request, neighborhood, city, state):
    placeID = getPhotos(neighborhood, city, state)

    print(placeID)
    response = HttpResponse(placeID)
    return response