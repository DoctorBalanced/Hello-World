### Tours App
#
# App that will take input latitude & longitude output poi
# API's used Opensky & GooglePlaces
# Opensky -> location and on-ground

from opensky_api import OpenSkyApi
from googleplaces import GooglePlaces, types, lang
import random

google_places = GooglePlaces('AIzaSyBUzRTaHauZm8TPdV-1lqpoAjeE6vXd0hg')
open_sky = OpenSkyApi()

#flight_number =  raw_input("What is your flight number? \n> ")
flights = open_sky.get_states()

random = random.randrange(0,len(flights.states))
callsign = flights.states[random].callsign

my_flight = {}
for flight in flights.states:
    if callsign == flight.callsign:
   	 my_flight = flight
   	 print(my_flight.origin_country)
   	 break

query_result = google_places.nearby_search(lat_lng={"lat": flight.latitude, "lng": flight.longitude}, radius=500000)
for place in query_result.places:
    print(place.name)
