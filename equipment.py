class NewCatch:
    def __init__(self):
        self.contents = {}  # composition over inheritance TODO: this will be a dict of items and quantities, e.g. {"cod": 3, "herring": 1}
    
    def __str__(self):
        return ""  # TODO: this will be a string representation of the catches, with the name and quantity

class NoFishingGear:
    def __init__(self):
        self.chances = {"nothing": 100}  # placeholder, other classes will overwrite this when inheriting

    def cast(self) -> NewCatch:
        return NewCatch()  # TODO: this will be a NewCatch object, will be generated based on the chances dict