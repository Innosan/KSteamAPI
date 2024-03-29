import requests

from main import MARKET_URL
from models.Error import Error
from models.MarketItem import parse_api_item


def parse_steam_item(item_title: str):
    try:
        response = requests.get(MARKET_URL + item_title)
    except:
        return {
            "status": False,
            "error": Error(400, "Steam request failure!")
        }
    # print(response)

    results = {}

    if response.json()['results']:
        results = response.json()['results'][0]
    else:
        return {
            "status": False,
            "error": Error(404, "Steam item parse failure!")
        }

    item = parse_api_item(results)

    return {
        "status": True,
        "item": item.to_dict()
    }
