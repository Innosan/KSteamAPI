import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

from models.CsMarketItem import MarketItem
from models.Error import Error

market_search_url = "https://market-old.csgo.com/?s=pop&search="
market_base_url = "https://market-old.csgo.com"


def parse_market_item(item_title: str):
    response = requests.get(market_search_url + quote(item_title) + "&sd=desc")
    soup = BeautifulSoup(response.content, 'html.parser')

    items = []
    souped_search_items = []

    market_items = soup.find("div", class_="market-items")
    # print(market_items)
    # print(soup)

    if market_items is not None:
        souped_search_items = market_items.find_all("a", class_="item").copy()
    else:
        return {
            "status": False,
            "error": Error(404, "Failed to fetch item due to server error!")
        }

    for souped_item in souped_search_items:
        item = MarketItem()

        item_image = (souped_item.find_next("div", class_="image")["style"].split("(")[1].split(")")[0])

        item.price = souped_item.find_next("div", class_="price").text
        item.title = souped_item.find_next("div", class_="name").text
        item.link = market_base_url + souped_item["href"]
        item.image = item_image

        items.append(item)

    return {
        "status": True,
        "items": [item.to_dict() for item in items]
    }
