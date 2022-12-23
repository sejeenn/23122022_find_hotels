import json
found_cities = {}
with open('data_with_err.json', 'r') as file:
    data = json.load(file)
    for string in data['sr']:
        try:

            found_cities[string['gaiaId']] = {
                "gaiaId": string['gaiaId'],
                "regionNames": string['regionNames']['fullName']
            }
        except KeyError:
            continue

for city in found_cities.values():
    print('Destination:', city['gaiaId'] + ', Город:', city['regionNames'])
