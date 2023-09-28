import requests
from bs4 import BeautifulSoup

from MarketItem import MarketItem

market_url = "https://market-old.csgo.com/?s=pop&t=all&sd=desc&search="


def parse_item(item_title: str):
    response = requests.get(market_url + item_title)
    soup = BeautifulSoup(response.content, 'html.parser')

    items = []

    souped_search_items = soup.find("div", class_="market-items").find_all("a", class_="item").copy()

    for souped_item in souped_search_items:
        item = MarketItem()

        item_image = (souped_item.find_next("div", class_="image")["style"].split("(")[1].split(")")[0])

        item.price = souped_item.find_next("div", class_="price").text
        item.title = souped_item.find_next("div", class_="name").text
        item.link = souped_item["href"]
        item.image = item_image

        items.append(item)

    return [item.to_dict() for item in items]
