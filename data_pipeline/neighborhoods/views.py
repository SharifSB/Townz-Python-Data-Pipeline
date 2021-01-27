from django.shortcuts import render
from django.http import HttpResponse
from .getNeighborhoodDescriptions import getDescriptions
# Create your views here.

def index(request, neighborhood, city, state):
    description = getDescriptions(neighborhood, city, state)
    print(neighborhood, city, state)
    response = HttpResponse(description)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
    return response