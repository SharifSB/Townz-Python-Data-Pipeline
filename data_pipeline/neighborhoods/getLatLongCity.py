from bs4 import BeautifulSoup
import requests
import json
import re
baseURL = "https://www.google.com/search?q="


def getLatLong(city, state):
    searchURL = baseURL + \
        "+".join(city.split("_")).title() + "+" + "+".join(state.split("_")).title() + "+" + "latitude+and+longitude"
    source = requests.get(searchURL).text
    descriptionToSend = ""

    
    soup = BeautifulSoup(source, "lxml")
    myElem = ""
    arr  = []
    for elem in soup(text=re.compile('°')):
        print(elem)
        # this = elem.parent.parent.parent.parent.parent
        # newSoup = BeautifulSoup(this.text, "lxml")
        myElem = elem.split(",")
        for elem in myElem:
            new = re.match('^(.*?)\°', elem)
            num = float(new[0].replace('°', ''))
            arr.append(num)
        
        break
        
    return arr
