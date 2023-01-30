import requests
import json

url = "https://hotels4.p.rapidapi.com/properties/v2/detail"

payload = {
    "currency": "USD",
    "eapid": 1,
    "locale": "en_US",
    "siteId": 300000001,
    "propertyId": "9209612"
}
headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": "25f90d3cdfmsh2cc6038b4e63c63p1d9fd5jsn2aad67a79b56",
    "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
}

response = requests.request("POST", url, json=payload, headers=headers)
data = response.json()
with open('search_hotel_detail.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

#print(response.text)
