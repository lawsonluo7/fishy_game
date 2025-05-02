import random

class NewCatch:
    def __init__(self, chances, amount):
        self.contents = {}
        self.chances = chances
        for i in range(amount):
            caught = self._catch()
            self.contents[caught] = self.contents.get(caught, 0) + 1

    def _catch(self):
        catch_chance = random.random() * 100
        chance_sum = 0
        for fish, curr_chance in self.chances.items():
            chance_sum += curr_chance
            if catch_chance <= chance_sum:
                return fish
    
    def __str__(self):
        formatted_contents = [f"{fish}: {amount}" for fish, amount in self.contents.items() if fish != "nothing"]
        return f"You caught:\n{"\n".join(formatted_contents)}" if formatted_contents else "Darn. You didn't catch anything. Womp Womp."
        
class NoFishingGear:
    def __init__(self):
        self.chances = {"nothing": 100.0}  # placeholder, other classes will overwrite this when inheriting

        self.capacity = 0

    def cast(self) -> NewCatch:
        return NewCatch(self.chances, self.capacity)  # TODO: this will be a NewCatch object, will be generated based on the chances dict