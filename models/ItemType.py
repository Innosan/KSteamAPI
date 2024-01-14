class ItemTypeManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ItemTypeManager, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.item_types = {
            "Covert Pistol": ItemType("Pistol", "dummy_icon_1"),
            "Covert Rifle": ItemType("Weapon", "dummy_icon_2"),
            "Base Grade Container": ItemType("Container", "dummy_icon_3"),
            "Base Grade Key": ItemType("Key", "dummy_icon_4"),
        }

    def get_type(self, item_type_str: str):
        if self.item_types.get(item_type_str) is not None:
            return self.item_types.get(item_type_str)
        else:
            return ItemType(item_type_str, "No icon found")


class ItemType:
    title: str
    icon: str

    def __init__(self, title: str, icon: str):
        self.title = title
        self.icon = icon
