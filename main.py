import equipment

class Purchase:
    def __init__(self, item: equipment.FishingGear, price: float):
        self.item = item
        self.price = price

class Game:
    shop = [
            Purchase(equipment.NoFishingGear(), 0.0),
            Purchase(equipment.WishDotComFishingRod(), 9.99),
        ]
            
class Player:
    def __init__(self):
        self.money: float = 10.00
        self.shop = Game.shop
        self.fishing_gear: Purchase = self.shop[0]

    def buy(self, index: int):
        self.sell_gear()
        if self.money >= self.shop[index].price:
            self.money -= self.shop[index].price
            self.fishing_gear = self.shop[index]

    def sell_gear(self):
        self.money += self.fishing_gear.price
        self.fishing_gear = self.shop[0]

    def cast(self):
        return self.fishing_gear.item.cast()