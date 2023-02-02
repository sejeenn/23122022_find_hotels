import json


def get_hotels(query_text):
    # попробуем расшифровать json с отелями
    print(query_text)
    possible_cities = {}
    data = json.loads(query_text)
    with open('data_hotels.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
    # if not data:
    #     raise LookupError('Запрос пуст...')
    # for id_place in data['sr']:
    #     try:
    #         possible_cities[id_place['gaiaId']] = {
    #             "gaiaId": id_place['gaiaId'],
    #             "regionNames": id_place['regionNames']['fullName']
    #         }
    #     except KeyError:
    #         continue
    # print(possible_cities)
    # return possible_cities
