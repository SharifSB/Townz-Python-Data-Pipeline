from django.urls import path, re_path
import re
from . import views

urlpatterns = [
    re_path(r'^(?P<neighborhood>[\w-]*)/(?P<city>[\w-]*)/(?P<state>[\w-]*)/$', views.index, name='index'),
]
