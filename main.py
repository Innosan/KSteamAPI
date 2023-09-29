from fastapi import FastAPI
from services.parse_cs_market import parse_market_item
from services.parse_steam_market import parse_steam_item

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/get-item/{item_title}")
async def get_item(item_title: str):
    market_items = parse_market_item(item_title)
    steam_item = parse_steam_item(item_title)

    return {
        "message": f"Getting {item_title}",
        "market_items": market_items,
        "steam_item": steam_item
    }


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
