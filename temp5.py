import json
import requests
url = "https://hotels4.p.rapidapi.com/properties/v2/get-summary"

payload = {
	"currency": "USD",
	"eapid": 1,
	"locale": "en_US",
	"siteId": 300000001,
	"propertyId": "82828743"
}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "25f90d3cdfmsh2cc6038b4e63c63p1d9fd5jsn2aad67a79b56",
	"X-RapidAPI-Host": "hotels4.p.rapidapi.com"
}

response = requests.request("POST", url, json=payload, headers=headers)
data = json.loads(response.text)
with open('get_summary.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4)

print(response.text)