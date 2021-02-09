from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .getListings import getListings
# Create your views here.

def getVacationRentals(request, city, state):
    data = getListings(city, state)
    response = JsonResponse(data, safe=False)
    return response