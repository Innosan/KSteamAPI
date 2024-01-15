from fastapi import FastAPI, Path
from fastapi.staticfiles import StaticFiles

from models.ItemType import ItemTypeManager

app = FastAPI()
item_type_manager = ItemTypeManager()

MARKET_URL = "https://steamcommunity.com/market/search/render/?appid=730&norender=1&query="
STEAM_URL = "https://steamcommunity.com/market/listings/730/"
IMAGE_URL = "https://steamcommunity-a.akamaihd.net/economy/image/"

from services.fetch_currency_rates import fetch_currency_rates
from services.parse_cs_market import parse_market_item
from services.parse_steam_market import parse_steam_item
from services.fetch_hot_items import fetch_hot_items


@app.get("/get-market-items/{item_title}")
async def get_market_items(item_title: str = Path(..., description="The title of the item", example="Glove Case")):
    market_items = parse_market_item(item_title)

    return market_items


@app.get("/get-steam-item/{item_title}")
async def get_steam_item(item_title: str = Path(..., description="The title of the item", example="Glove Case")):
    steam_item = parse_steam_item(item_title)

    return steam_item


@app.get("/get-hot-items")
async def get_hot_items():
    hot_items = fetch_hot_items()

    return hot_items


@app.get("/get-currency-rates")
async def get_currency_rates():
    currency_rates = fetch_currency_rates()

    return {
        "status": currency_rates["status"],
        "currency_rates": currency_rates["rates"]
    }


@app.get("/get-item-types")
async def get_item_types():
    return list(item_type_manager.item_types.values())


app.mount("/", StaticFiles(directory="static", html=True), name="static")
