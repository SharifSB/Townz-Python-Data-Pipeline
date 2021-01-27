from bs4 import BeautifulSoup
import requests
import json
import re
baseURL = "https://www.google.com/search?q="


def getDescriptions(neighborhood, city, state):
    string = r'^.*?' + state
    searchURL = baseURL + \
        "+".join(neighborhood.split("_")) + "+" + "+".join(city.split("_"))
    source = requests.get(searchURL).text
    descriptionToSend = ""
    soup = BeautifulSoup(source, "lxml")
    print(soup)
    for elem in soup(text=re.compile("((Commercial |Residential )[Nn]eighborhood|Neighborhood) in")):
        this = elem.parent.parent.parent.parent.parent
        newSoup = BeautifulSoup(this.text, "lxml")
        descriptionToSend = (newSoup.find(
            "p").text).replace(" ".join(neighborhood.split("_")), "", 1)
        
        formattedDescription = re.match(string, descriptionToSend)
        descriptionToSend = descriptionToSend.replace(formattedDescription[0], "", 1)
        
    return descriptionToSend
