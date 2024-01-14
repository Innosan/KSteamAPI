import requests

from models.Error import Error
from models.MarketItem import MarketItem

market_url = "https://steamcommunity.com/market/search/render/?appid=730&norender=1&query="
steam_link = "https://steamcommunity.com/market/listings/730/"


def parse_steam_item(item_title: str):
    try:
        response = requests.get(market_url + item_title)
    except:
        return Error(400, "Steam request failure!")
    print(response)

    results = {}

    if response.json()['results']:
        results = response.json()['results'][0]
    else:
        return Error(404, "Steam item parse failure!")

    item = MarketItem()
    item.price = results["sell_price_text"]
    item.title = results["name"]
    item.link = steam_link + item.title

    return item.to_dict()
