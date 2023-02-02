import requests
from config_data import config
headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": config.RAPID_API_KEY,
    "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
}
url = "https://hotels4.p.rapidapi.com/locations/v3/search"


def find_destination(city):
    querystring = {"q": city, "locale": "en_US"}
    query = requests.request("GET", url, params=querystring, headers=headers)
    print(query.text)

