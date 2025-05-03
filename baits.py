import random

class NoBait:
    def __init__(self):
        self.chances: dict = {"nothing": 100.0}  # placeholder, other classes will overwrite this when inheriting
        self.weight: float = 0.0

    def lure(self) -> str:
        catch_chance: float = random.random() * 100
        chance_sum: float = 0.0
        for fish, curr_chance in self.chances.items():
            chance_sum += curr_chance
            if catch_chance <= chance_sum:
                return fish
        

# values for next bait:  {"nothing": 46.0, "cod": 20.0, "tuna": 18.0, "salmon": 16.0}, I do not know much about fish, feel free to pull request on github with more realistic chances
