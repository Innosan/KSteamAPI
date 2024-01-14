import requests

from models.Error import Error
from models.MarketItem import MarketItem

market_url = "https://steamcommunity.com/market/search/render/?appid=730&norender=1&query="
steam_url = "https://steamcommunity.com/market/listings/730/"
image_url = "https://steamcommunity-a.akamaihd.net/economy/image/"


def parse_steam_item(item_title: str):
    try:
        response = requests.get(market_url + item_title)
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

    item = MarketItem()
    item.price = results["sell_price_text"]
    item.title = results["name"]
    item.link = steam_url + item.title
    item.image = image_url + results["asset_description"]["icon_url"]

    return {
        "status": True,
        "item": item.to_dict()
    }
