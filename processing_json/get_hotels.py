import json


def get_hotels(query_text):
    # попробуем расшифровать json с отелями
    data = json.loads(query_text)
    if not data:
        raise LookupError('Запрос пуст...')
    hotels_data = {}
    for hotel in data['data']['propertySearch']['properties']:
        try:
            hotels_data[hotel['id']] = {
                'name': hotel['name'], 'id': hotel['id'],
                'picture': hotel['propertyImage']['image']['url'],
                'distance': hotel['destinationInfo']['distanceFromDestination']['value'],
                'unit': hotel['destinationInfo']['distanceFromDestination']['unit'],
                'price': hotel['price']['options'][0]['strikeOut']['formatted']
            }
        except (KeyError, TypeError):
            continue
    return hotels_data
