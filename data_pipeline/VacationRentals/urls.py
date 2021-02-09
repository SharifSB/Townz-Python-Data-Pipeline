from django.urls import path, re_path
import re
from . import views

urlpatterns = [
re_path(r'vacation/(?P<city>[\w-]*)/(?P<state>[\w-]*)/any/0', views.getVacationRentals, name='index'),
]
