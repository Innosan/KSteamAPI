class CsMarketItem:
    image: str
    title: str
    price: str
    link: str

    def __str__(self):
        return (
            f"<CS Market item title:{self.title},"
            f" price:{self.price},"
            f" image: {self.image},"
            f" link: {self.link}>"
        )

    def to_dict(self):
        cleaned_title = self.title.strip().replace("\n", "")
        cleaned_price = self.price.strip().replace(" ", "")
        cleaned_link = self.link

        # return a dictionary with the attributes of the object
        return {
            "title": cleaned_title,
            "price": cleaned_price,
            "image": self.image,
            "link": cleaned_link
        }
