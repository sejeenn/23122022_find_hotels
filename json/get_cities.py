import json


def get_city(query):
    possible_cities = {}
    data = json.loads(query.text)
    if not data:
        raise LookupError('Запрос пуст...')
    for id_place in data['sr']:
        try:
            possible_cities[id_place['gaiaId']] = {
                "gaiaId": id_place['gaiaId'],
                "regionNames": id_place['regionNames']['fullName']
                }
        except KeyError:
            continue