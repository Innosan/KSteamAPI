from models.ItemType import ItemType
from models.MarketApp import MarketApp


class MarketItem:
    def __init__(self, title: str, price: str, link: str, image: str, item_type: ItemType, app: MarketApp):
        self.title = title
        self.price = price
        self.link = link
        self.image = image
        self.item_type = item_type
        self.app = app

    title: str
    price: str
    link: str
    image: str
    item_type: ItemType
    app: MarketApp

    def to_dict(self):
        # return a dictionary with the attributes of the object
        return {
            "title": self.title,
            "price": self.price,
            "link": self.link,
            "image": self.image,
            "item_type": self.item_type,
            "app": self.app
        }
