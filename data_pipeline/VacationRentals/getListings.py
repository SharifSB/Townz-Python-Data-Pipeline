import airbnb
api = airbnb.Api()
def getListings(city, state):

    listings = api.get_homes(" ".join(city.split("_")))
    return listings