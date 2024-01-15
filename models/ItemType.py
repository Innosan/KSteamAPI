class ItemTypeManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ItemTypeManager, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.item_types = {
            "Covert Pistol": ItemType("Pistol", "i-mdi-pistol"),
            "Covert Rifle": ItemType("Weapon", "i-game-icons-winchester-rifle"),
            "Base Grade Container": ItemType("Container", "i-lucide-container"),
            "Base Grade Key": ItemType("Key", "i-material-symbols-key-vertical-outline-rounded"),
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
