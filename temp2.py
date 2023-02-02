import requests
import processing_json
url = "https://hotels4.p.rapidapi.com/properties/v2/list"
data = {'command': '/lowprice', 'sort': 'PRICE_LOW_TO_HIGH', 'date_time': '26.12.2022 09:12:20',
        'telegram_id': 732418186, 'chat_id': 732418186, 'input_city': 'rome', 'destination_id': '5194566',
        'quantity_hotels': '4', 'price_min': '100', 'price_max': '150', 'photo_need': 'no', 'photo_count': '0',
        'checkInDate': {'day': 26, 'month': 12, 'year': 2022}, 'checkOutDate': {'day': 31, 'month': 12,
                                                                                      'year': 2022}}

# payload = {
#     "currency": "USD",
#     "eapid": 1,
#     "locale": "en_US",
#     "siteId": 300000001,
#     "destination": {"regionId": "492"},
#     "checkInDate": {
#         "day": 10,
#         "month": 10,
#         "year": 2022
#     },
#     "checkOutDate": {
#         "day": 15,
#         "month": 10,
#         "year": 2022
#     },
#     "rooms": [
#         {
#             "adults": 2,
#             "children": [{"age": 5}, {"age": 7}]
#         }
#     ],
#     "resultsStartingIndex": 0,
#     "resultsSize": 200,
#     "sort": "PRICE_LOW_TO_HIGH",
#     "filters": {"price": {
#         "max": 150,
#         "min": 100
#     }}
# }
payload = {
        "currency": "USD",
        # "eapid": 1,
        "locale": "en_US",
        # "siteId": 300000001,
        "destination": {"regionId": data['destination_id']},
        "checkInDate": data['checkInDate'],
        "checkOutDate": data['checkOutDate'],
        "rooms": [
            {
                "adults": 2
            }
        ],
        "resultsStartingIndex": 0,
        "resultsSize": int(data["quantity_hotels"]),
        "sort": data['sort'],
        "filters": {"price": {
            "max": int(data['price_max']),
            "min": int(data['price_min'])
        }}
    }

headers = {
    "content-type": "application/processing_json",
    "X-RapidAPI-Key": "25f90d3cdfmsh2cc6038b4e63c63p1d9fd5jsn2aad67a79b56",
    "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
}

response = requests.request("POST", url, json=payload, headers=headers)
data = response.json()
with open('find_hotels.json', 'w', encoding='utf-8') as f:
    processing_json.dump(data, f, ensure_ascii=False, indent=4)
print(response.status_code)
print(response.text)
print(payload)