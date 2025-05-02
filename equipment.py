import random

class NewCatch:
    def __init__(self, chances, amount):
        self.contents = {}
        self.chances = chances
        for i in range(amount):
            self.contents[self._catch()] += self.contents.get(self._catch(), 0)

        
    def _catch(self):
        catch_chance = random.random() * 100
        chance_sum = 0
        for fish, curr_chance in self.chances.items():
            chance_sum += curr_chance
            if catch_chance <= chance_sum:
                return fish
    
    def __str__(self):
        return f"You caught:\n{"\n".join([fish + ": " + fish for fish, amount in self.contents.items() if amount != "nothing"])}"
        
class NoFishingGear:
    def __init__(self):
        self.chances = {"nothing": 100.0}  # placeholder, other classes will overwrite this when inheriting

        self.capacity = 0

    def cast(self) -> NewCatch:
        return NewCatch(self.chances, self.capacity)  # TODO: this will be a NewCatch object, will be generated based on the chances dict

c = NewCatch({"cod": 25.0, "nothing": 50.0, "salmon": 25.0"}, 5)
print(c)