from fastapi import FastAPI, Path
from fastapi.staticfiles import StaticFiles

from models.ItemType import ItemTypeManager
from services.fetch_currency_rates import fetch_currency_rates
from services.parse_cs_market import parse_market_item
from services.parse_steam_market import parse_steam_item

app = FastAPI()
item_type_manager = ItemTypeManager()


@app.get("/get-item/{item_title}")
async def get_item(item_title: str = Path(..., description="The title of the item", example="Glove Case")):
    market_items = parse_market_item(item_title)
    steam_item = parse_steam_item(item_title)

    return {
        "status": market_items["status"] | steam_item["status"],
        "market_items": market_items,
        "steam_item": steam_item
    }


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
