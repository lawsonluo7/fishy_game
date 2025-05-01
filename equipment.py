class NewCatch(dict):
    def __str__(self):
        return ""  # TODO: this will be a string representation of the catch, with the name and quantity

class NoFishingGear:
    def __init__(self):
        self.chances = {"nothing": 100}  # placeholder, other classes will overwrite this

    def cast(self) -> NewCatch:
        return NewCatch()  # TODO: this will be a NewCatch object, will be generated based on the chances dict