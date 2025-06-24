import baits
import time
import random
import logging

class NewCatch:
    def __init__(self, bait: baits.NoBait, amount: int):
        self.contents: dict = {}
        self.prices: dict = {
            "nothing": 0.0,
            "cod": 2.50,
            "tuna": 3.00,
            "salmon": 4.00,
        }
        actual_sleep = time.time()
        time.sleep(bait.wait_time * (random.random() / 2 + 0.75))
        actual_sleep = time.time() - actual_sleep
        logging.debug(f"sleep time: {actual_sleep:.2f} seconds")
        for i in range(amount):
            caught = bait.lure()
            self.contents[caught] = self.contents.get(caught, 0) + 1

    def to_money(self) -> float:
        total = 0.0
        for fish, amount in self.contents.items():
            if fish != "nothing":
                total += self.prices[fish] * amount * (random.random() / 2 + 0.75)
        return round(total, 2)
