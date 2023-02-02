import json
import requests
from config_data import config
from loguru import logger

url = "https://hotels4.p.rapidapi.com/properties/v2/list"

payload = {
	"currency": "USD",
	"eapid": 1,
	"locale": "en_US",
	"siteId": 300000001,
	"destination": {"regionId": "492"},
	"checkInDate": {
		"day": 10,
		"month": 10,
		"year": 2022
	},
	"checkOutDate": {
		"day": 15,
		"month": 10,
		"year": 2022
	},
	"rooms": [
		{
			"adults": 2,
			"children": [{"age": 5}, {"age": 7}]
		}
	],
	"resultsStartingIndex": 0,
	"resultsSize": 200,
	"sort": "PRICE_LOW_TO_HIGH",
	"filters": {"price": {
			"max": 150,
			"min": 100
		}}
}
headers = {
	"content-type": "application/processing_json",
	"X-RapidAPI-Key": "25f90d3cdfmsh2cc6038b4e63c63p1d9fd5jsn2aad67a79b56",
	"X-RapidAPI-Host": "hotels4.p.rapidapi.com"
}

response = requests.request("POST", url, json=payload, headers=headers)

#print(response.text)