import json
import requests
from config_data import config
from loguru import logger

headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": config.RAPID_API_KEY,
    "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
}


def test_request(query):
    try:
        print(query.status_code)
        if query.status_code != 200:
            raise LookupError(f'Status code {query.status_code}')
        if not query:
            return {}
        data = json.loads(query.text)
        if not data:
            raise LookupError('Запрос пуст...')
        return query
    except (LookupError, TypeError) as exc:
        logger.error(exc, exc_info=exc)


def request(method, url, query_string):
    print('Запрос к серверу')

    if method == "GET":
        query_get = requests.request("GET", url, params=query_string, headers=headers)
        return test_request(query_get)
    elif method == "POST":
        query_post = requests.request("POST", url, json=query_string, headers=headers)

