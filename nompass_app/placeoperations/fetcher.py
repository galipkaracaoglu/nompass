import requests
import urllib.request
from . import place 


firstpart ="https://maps.googleapis.com/maps/api/place/textsearch/json?query="


key="&key=AIzaSyDMrR0jNFRLc1c6PL9ed3jDpcZrRBmx8k4"






def extractPlace(text):
    r = requests.get(firstpart+text+key)
    json_form =r.json()["results"]
    my_results = ""
    for pl in json_form:
        name=pl["name"]
        adress=pl["formatted_address"]
        lat=pl["geometry"]["location"]["lat"]
        lot=pl["geometry"]["location"]["lng"]
        my_results = my_results +  name + "--->" + adress + "<br></br>"
    return my_results


   



extractPlace("ITÜ teknokent")

