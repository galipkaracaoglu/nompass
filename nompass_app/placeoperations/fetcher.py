import requests
import urllib.request
from . import place 
import psycopg2
from db import database
import random

firstpart ="https://maps.googleapis.com/maps/api/place/textsearch/json?query="


key="&key=AIzaSyDMrR0jNFRLc1c6PL9ed3jDpcZrRBmx8k4"


"""
"formatted_address" : "Sinanpaşa Mahallesi, 34353 Beşiktaş/İstanbul, Türkiye",

"""


def loadPlaces():
    places=place.Place.query.all()
    results = []
    for pl in places:
        results.append(pl.name)
    return results


def extractPlace(text):
    r = requests.get(firstpart+text+key)
    json_form =r.json()["results"]
    my_results = ""
    for pl in json_form:
        name=pl["name"]
        adress=pl["formatted_address"]


        lat=pl["geometry"]["location"]["lat"]
        lot=pl["geometry"]["location"]["lng"]

        database.engine.execute("INSERT INTO \"Place\" (id, name,adress,cordinate_lat,cordinate_lot, general_point,city,semt) VALUES (" + str(random.randint(0,10000)) + ",'" + name +  "','','','',0,'İstanbul','');")


        
        my_results = my_results +  name + "--->" + adress + "<br></br>"
    return my_results


   

