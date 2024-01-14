class MarketItem:
    def __init__(self):
        pass

    title: str
    price: str
    link: str
    image: str

    def to_dict(self):
        # return a dictionary with the attributes of the object
        return {
            "title": self.title,
            "price": self.price,
            "link": self.link,
            "image": self.image
        }
