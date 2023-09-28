from fastapi import FastAPI
from parse_cs_market import parse_item

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/get-item/{item_title}")
async def get_item(item_title: str):
    market_items = parse_item(item_title)
    return {"message": f"Getting {item_title}", "market_items": market_items}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
