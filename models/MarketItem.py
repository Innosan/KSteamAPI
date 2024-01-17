from main import STEAM_URL, IMAGE_URL
from models.ItemType import ItemType, ItemTypeManager
from models.MarketApp import MarketApp


class MarketItem:
    def __init__(self, title: str, price: str, link: str, image: str, item_type: ItemType, app: MarketApp):
        self.title = title
        self.price = price.replace('$', '')
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


def parse_api_item(api_item):
    item_assets = api_item["asset_description"]
    item_type_manager = ItemTypeManager()

    item = MarketItem(
        title=api_item["name"],
        price=api_item["sell_price_text"],
        link=STEAM_URL + api_item["name"],  # Assuming steam_url is defined elsewhere
        image=IMAGE_URL + item_assets["icon_url"],  # Assuming image_url is defined elsewhere
        item_type=item_type_manager.get_type(item_assets["type"]),
        app=MarketApp(
            id=item_assets["appid"],
            title=api_item["app_name"],
            icon=api_item["app_icon"]
        )
    )

    return item
