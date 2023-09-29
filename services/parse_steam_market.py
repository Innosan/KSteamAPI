import requests

from models.MarketItem import MarketItem

market_url = "https://steamcommunity.com/market/search/render/?appid=730&norender=1&query="
steam_link = "https://steamcommunity.com/market/listings/730/"


def parse_steam_item(item_title: str):
    response = requests.get(market_url + item_title)
    results = response.json()['results'][0]

    item = MarketItem()
    item.price = results["sell_price_text"]
    item.title = results["name"]
    item.link = steam_link + item_title

    return item.to_dict()
