import requests

from models.Error import Error
from models.ItemType import ItemTypeManager
from models.MarketApp import MarketApp
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

    item_assets = results["asset_description"]
    item_type_manager = ItemTypeManager()

    item = MarketItem(
        title=results["name"],
        price=results["sell_price_text"],
        link="",
        image=image_url + item_assets["icon_url"],
        item_type=item_type_manager.get_type(item_assets["type"]),
        app=MarketApp(
            id=item_assets["appid"],
            title=results["app_name"],
            icon=results["app_icon"]
        )
    )

    item.link = steam_url + item.title

    return {
        "status": True,
        "item": item.to_dict()
    }
