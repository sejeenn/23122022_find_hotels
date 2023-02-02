import requests
from config_data import config
headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": config.RAPID_API_KEY,
    "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
}
url = "https://hotels4.p.rapidapi.com/properties/v2/list"


payload = {'currency': 'USD',  'locale': 'en_US',
           'destination': {'regionId': '553248633938945217'}, 'checkInDate': {'day': 23, 'month': 2, 'year': 2023},
           'checkOutDate': {'day': 25, 'month': 2, 'year': 2023},
           'rooms': [{'adults': 2}], 'resultsStartingIndex': 0,
           'resultsSize': 5, 'sort': 'PRICE_LOW_TO_HIGH', 'filters': {'price': {'max': '7', 'min': '6'}
                                                                      }
           }


response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)
