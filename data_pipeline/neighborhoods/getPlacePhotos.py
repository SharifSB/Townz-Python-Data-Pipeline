import requests 
import json
baseURL = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input="
apiKey = "&key=AIzaSyBO_WspjC-jheeQbPUJVjX_dPcLVhOIwFs"
params = "&inputtype=textquery&fields=photos"
def getPhotos(neighborhood, city, state):
    FullURL = baseURL + "%20".join(neighborhood.split("_")) + "%20" + "%20".join(city.split("_")) + params + apiKey
    data = requests.get(FullURL).json()
    return data