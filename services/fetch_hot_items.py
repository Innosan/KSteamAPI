import requests

from models.Error import Error
from models.MarketItem import parse_api_item

market_url = "https://steamcommunity.com/market/search/render/?norender=1&appid=730&count=5"


def fetch_hot_items():
    try:
        response = requests.get(market_url)
    except:
        return {
            "status": False,
            "error": Error(400, "Steam request failure!")
        }

    results = []

    if response.json()['results']:
        results = response.json()['results']
    else:
        return {
            "status": False,
            "error": Error(404, "Steam item parse failure!")
        }

    hot_items = []
    for result in results:
        hot_items.append(parse_api_item(result))

    return hot_items
