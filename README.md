# 🔑 KSteamAPI
**API for an web/mobile app for checking prices and profits of the Steam Market items**

## ℹ️ Info
The primary goal of this project is to empower CS:GO enthusiasts with a tool that simplifies the process of finding and accessing detailed information about CS:GO items. 

In addition to parsing CS:GO market search results, **future** plans for the project include integrating Steam functionality. This will allow users to perform actions such as counting **wishlisted games** within their selected items and viewing the sale prices of items on Steam.

## ⚙️ Key Features
- Parse CS:GO market search query pages based on user-selected items
- Retrieve detailed information about available items
- Integration with Steam for additional functionality in the future

## ⤴️ Routes
- **GET /get-item/{item_title}** - Retrieve all available items matching the given item title
- *(Future)* **GET /steam/wishlist** - Count wishlisted games within user-selected items
- *(Future)* **GET /steam/sale/{item_name}** - Retrieve the sale price of an item on Steam

## 📚 Resources
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [CS:GO Market](https://market-old.csgo.com/)
- [Design](https://www.figma.com/file/f1i6azCL75xIw4BViTGiOn/KSteam?type=design&node-id=0%3A1&mode=design&t=XBZxYWcFWZRMHtw0-1)
