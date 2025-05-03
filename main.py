import baits
import fishing_gear
import new_catch

class Purchase:
    def __init__(self, item, price: float):
        self.item = item
        self.price = price

class Game:
    fishing_gear_shop = [
            Purchase(fishing_gear.NoFishingGear(), 0.0),
            Purchase(fishing_gear.WishDotComFishingRod(baits.NoBait()), 9.99),
        ]
    bait_shop = [
            Purchase(baits.NoBait(), 0.0),
        ]

game = Game()

class Player:
    def __init__(self):
        self.money: float = 10.00
        self.bait_shop = game.bait_shop
        self.fishing_gear_shop = game.fishing_gear_shop
        self.fishing_gear: Purchase = self.fishing_gear_shop[0]
        self.bait: Purchase = self.bait_shop[0]

    def buy(self, index: int) -> None:
        self.sell_fishing_gear()
        if self.money >= self.fishing_gear_shop[index].price:
            self.money -= self.fishing_gear_shop[index].price
            self.fishing_gear = self.fishing_gear_shop[index]

    def sell_fishing_gear(self) -> None:
        self.money += self.fishing_gear.price
        self.fishing_gear = self.fishing_gear_shop[0]

    def buy_bait(self, index: int) -> None:
        self.sell_bait()
        if self.money >= self.bait_shop[index].price:
            self.money -= self.bait_shop[index].price
            self.bait = self.bait_shop[index]

    def sell_bait(self) -> None:
        self.money += self.bait.price
        self.bait = self.bait_shop[0]

    def cast(self) -> new_catch.NewCatch:
        return self.fishing_gear.item.cast()

def test_player_buy():
    player = Player()
    print(f"Got: {player.money}, Expected: 10.00")
    print("Testing player money is 10.00")
    player.buy(1)
    print(f"Got: {player.money}, Expected: 0.01")
    print("Testing player money after buying fishing rod")
    print(f"Got: {player.fishing_gear.item}, Expected: {fishing_gear.WishDotComFishingRod(baits.NoBait())}")
    print("Testing player's fishing gear is WishDotComFishingRod")

def test_player_sell_gear():
    player = Player()
    player.buy(1)
    print(f"Got: {player.money}, Expected: 0.01")
    print("Testing player money after buying fishing rod")
    player.sell_fishing_gear()
    print(f"Got: {player.money}, Expected: 10.00")
    print("Testing player money after selling fishing rod")
    print(f"Got: {player.fishing_gear.item}, Expected: {fishing_gear.NoFishingGear()}")
    print("Testing player's fishing gear is NoFishingGear")

def test_player_cast():
    player = Player()
    player.buy(1)
    print(f"Got: {isinstance(player.cast(), new_catch.NewCatch)}, Expected: True")
    print("Testing if the cast is a new catch")

if __name__ == "__main__":
    test_player_buy()
    test_player_sell_gear()
    test_player_cast()