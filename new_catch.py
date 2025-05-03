import baits

class NewCatch:
  def __init__(self, bait, amount: int):
      self.contents: dict = {}
      for i in range(amount):
          caught = bait.lure()
          self.contents[caught] = self.contents.get(caught, 0) + 1


  def __str__(self) -> str:
      formatted_contents = [
          f"{fish}: {amount}"
          for fish, amount in self.contents.items()
          if fish != "nothing"
      ]

      if not formatted_contents:
          message = "Darn. You didn't catch anything. Womp Womp."
      elif len(formatted_contents) == 1:
          message = f"You caught a {list(self.contents.keys())[0]}"
      else:
          message = f"You caught:\n{"\n".join(formatted_contents)}"
          
      return message
