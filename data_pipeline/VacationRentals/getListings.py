import airbnb
api = airbnb.Api()
def getListings(city, state):

    listings = api.get_homes("Ocean-Beach, San Diego, CA", items_per_grid=300, checkin="2021-03-26", checkout="2021-03-28")
    print(len(listings))
    return listings