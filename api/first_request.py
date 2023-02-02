import json
import requests
from config_data import config
from loguru import logger

# locations/v3/search - поиск локации по названию
# properties/v2/list - получение списка отелей по региону
# properties/v2/detail - подробнее об отеле - адрес, фотки

headers = {
    "content-type": "application/processing_json",
    "X-RapidAPI-Key": config.RAPID_API_KEY,
    "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
}
url = "https://hotels4.p.rapidapi.com/locations/v3/search"


def find_destination(city: str):
    logger.info('Программа перешла к поиску города: ' + city)
    querystring = {"q": city, "locale": "en_US"}
    possible_cities = {}
    try:
        query = requests.request("GET", url, params=querystring, headers=headers)
        if query.status_code != 200:
            raise LookupError(f'Status code {query.status_code}')
        if not query:
            return {}
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

        return possible_cities
    except (LookupError, TypeError) as exc:
        logger.error(exc, exc_info=exc)
