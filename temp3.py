import requests

url = "https://hotels4.p.rapidapi.com/reviews/v3/list"

payload = {
	"currency": "USD",
	"eapid": 1,
	"locale": "en_US",
	"siteId": 300000001,
	"propertyId": "9209612",
	"size": 10,
	"startingIndex": 0
}
headers = {
	"content-type": "application/processing_json",
	"X-RapidAPI-Key": "25f90d3cdfmsh2cc6038b4e63c63p1d9fd5jsn2aad67a79b56",
	"X-RapidAPI-Host": "hotels4.p.rapidapi.com"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)