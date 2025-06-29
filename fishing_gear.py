import new_catch
import baits

class NoFishingGear:
  def __init__(self):
      self.fish_capacity: int = 0
      self.max_bait_weight: float = 0.0
      self.bait: baits.NoBait = baits.NoBait()

  def cast(self) -> new_catch.NewCatch:
      if self.bait.weight <= self.max_bait_weight:
          return new_catch.NewCatch(self.bait, self.fish_capacity)
      else:
          return new_catch.NewCatch(baits.NoBait(), 0)

class TemuFishingRod(NoFishingGear):
    def __init__(self, bait = baits.NoBait()):
        self.fish_capacity = 1
        self.bait = bait
        self.max_bait_weight = 0.8