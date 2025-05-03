import new_catch
import baits
import new_catch

class NoFishingGear:
  def __init__(self):
      self.fish_capacity: int = 0
      self.max_bait_weight: float = 0.0
      self.bait: baits.NoBait = baits.NoBait()

  def cast(self) -> new_catch.NewCatch:
      if self.bait.weight <= self.max_bait_weight:
          return new_catch.NewCatch(self.chances, self.fish_capacity)
      else:
          return new_catch.NewCatch(NoBait(), 0)

class WishDotComFishingRod(NoFishingGear):
  def __init__(self, bait = baits.NoBait):
      self.fish_capacity: int = 1
      self.max_bait_weight: float = 0.8
      self.bait = bait
      