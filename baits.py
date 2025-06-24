import random

class NoBait:
    def __init__(self):
        self.chances: dict = {"nothing": 100.0}  # placeholder, other classes will overwrite this when inheriting
        self.weight: float = 0.0
        self.wait_time: float = 0.0

    def lure(self) -> str:
        catch_chance: float = random.random() * 100
        chance_sum: float = 0.0
        for fish_name, curr_chance in self.chances.items():
            chance_sum += curr_chance
            if catch_chance <= chance_sum:
                return fish_name

class WishDotComBait(NoBait):
    def __init__(self):
        self.chances = {"nothing": 46.0, "cod": 20.0, "tuna": 18.0, "salmon": 16.0}
        self.weight = 0.5
        self.wait_time = 3.5

class NormalBait(NoBait):
    def __init__(self):
        self.chances = {"nothing": 20.0, "cod": 30.0, "tuna": 25.0, "salmon": 25.0}
        self.weight = 0.75
        self.wait_time = 2.5
