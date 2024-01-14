class MarketApp:
    id: int
    title: str
    icon: str

    def __init__(self, id: int, title: str, icon: str):
        self.id = id
        self.title = title
        self.icon = icon
