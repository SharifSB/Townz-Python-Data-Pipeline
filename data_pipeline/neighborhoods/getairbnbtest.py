
from bs4 import BeautifulSoup
import requests
import json
import re
baseURL = "https://www.airbnb.com/s/Ocean-Beach--San-Diego--CA--United-States/homes?refinement_paths%5B%5D=%2Fhomes&tab_id=home_tab&checkin=2021-03-29&checkout=2021-03-31&search_type=unknown&date_picker_type=calendar&&ne_lat=32.79347474380189&ne_lng=-117.1795006178113&sw_lat=32.7111259988505&sw_lng=-117.28922657205521&zoom=13&search_by_map=true"


def getListings():
    searchURL = baseURL 
    source = requests.get(searchURL).text
    soup = BeautifulSoup(source, "lxml")
    return soup
