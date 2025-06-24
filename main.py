import baits
import fishing_gear
import new_catch
import tkinter as tk
from tkinter import ttk, messagebox
import random
import time

class Purchase:
    def __init__(self, item, price: float):
        self.product = item
        self.price = price

class Player:
    def __init__(self, game):
        self.money: float = 12.50
        self.days_played: int = 0
        self.bait_shop = game.bait_shop
        self.fishing_gear_shop = game.fishing_gear_shop
        self.fishing_gear_purchase: Purchase = self.fishing_gear_shop[0]
        self.bait_purchase: Purchase = self.bait_shop[0]

    def buy(self, index: int) -> None:
        self.sell_fishing_gear()
        if self.money >= self.fishing_gear_shop[index].price:
            self.money = round(self.money - self.fishing_gear_shop[index].price, 2)
            self.fishing_gear_purchase = self.fishing_gear_shop[index]

    def sell_fishing_gear(self) -> None:
        self.money = round(self.money + self.fishing_gear_purchase.price, 2)
        self.fishing_gear_purchase = self.fishing_gear_shop[0]

    def buy_bait(self, index: int) -> None:
        self.sell_bait()
        if self.money >= self.bait_shop[index].price:
            self.money = round(self.money - self.bait_shop[index].price, 2)
            self.bait_purchase = self.bait_shop[index]
            self.fishing_gear_purchase.product.bait = self.bait_purchase.product  # Set the bait on the fishing gear

    def sell_bait(self) -> None:
        self.money = round(self.money + self.bait_purchase.price, 2)
        self.bait_purchase = self.bait_shop[0]
        self.fishing_gear_purchase.product.bait = self.bait_purchase.product  # Reset bait when selling

    def cast(self) -> new_catch.NewCatch:
        self.days_played += 1
        return self.fishing_gear_purchase.product.cast()

class FishingGame:
    def __init__(self, root):
        self.fishing_gear_shop = [
            Purchase(fishing_gear.NoFishingGear(), 0.0),
            Purchase(fishing_gear.TemuFishingRod(), 9.99),
        ]
        self.bait_shop = [
            Purchase(baits.NoBait(), 0.0),
        Purchase(baits.WishDotComBait(), 2.49),
Purchase(baits.NormalBait(), 4.99)
        ]

        self.root = root
        self.root.title("Fishing Game")
        self.player = Player(self)

        # Create main frame
        self.main_frame = ttk.Frame(root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Money and Days display
        self.money_var = tk.StringVar(value=f"Money: ${self.player.money:.2f}")
        self.days_var = tk.StringVar(value=f"Days: {self.player.days_played}")
        ttk.Label(self.main_frame, textvariable=self.money_var).grid(row=0, column=0, pady=5)
        ttk.Label(self.main_frame, textvariable=self.days_var).grid(row=0, column=1, pady=5)

        # Fishing Gear Section
        ttk.Label(self.main_frame, text="Fishing Gear:").grid(row=1, column=0, columnspan=2, pady=5)
        self.gear_var = tk.StringVar()
        self.gear_combo = ttk.Combobox(self.main_frame, textvariable=self.gear_var, state='readonly')
        self.gear_combo['values'] = [f"{gear.product.__class__.__name__} (${gear.price:.2f})"
                                   for gear in self.player.fishing_gear_shop]
        self.gear_combo.grid(row=2, column=0, pady=5)
        self.gear_combo.set(f"{self.player.fishing_gear_purchase.product.__class__.__name__} (${self.player.fishing_gear_purchase.price:.2f})")

        self.buy_gear_button = ttk.Button(self.main_frame, text="Buy Gear", command=self.buy_gear)
        self.buy_gear_button.grid(row=2, column=1, padx=5)

        # Bait Section
        ttk.Label(self.main_frame, text="Bait:").grid(row=3, column=0, columnspan=2, pady=5)
        self.bait_var = tk.StringVar()
        self.bait_combo = ttk.Combobox(self.main_frame, textvariable=self.bait_var, state='readonly')
        self.bait_combo['values'] = [f"{bait.product.__class__.__name__} (${bait.price:.2f})"
                                   for bait in self.player.bait_shop]
        self.bait_combo.grid(row=4, column=0, pady=5)
        self.bait_combo.set(f"{self.player.bait_purchase.product.__class__.__name__} (${self.player.bait_purchase.price:.2f})")

        self.buy_bait_button = ttk.Button(self.main_frame, text="Buy Bait", command=self.buy_bait)
        self.buy_bait_button.grid(row=4, column=1, padx=5)

        # Cast Button
        self.cast_button = ttk.Button(self.main_frame, text="Cast Line!", command=self.cast)
        self.cast_button.grid(row=5, column=0, columnspan=2, pady=20)

        # Result Display
        self.result_var = tk.StringVar(value="Cast your line to start fishing!")
        ttk.Label(self.main_frame, textvariable=self.result_var, wraplength=200).grid(row=6, column=0, columnspan=2, pady=5)

    def update_displays(self):
        self.money_var.set(f"Money: ${self.player.money:.2f}")
        self.days_var.set(f"Days: {self.player.days_played}")

    def _disable_controls(self):
        self.gear_combo.config(state='disabled')
        self.bait_combo.config(state='disabled')
        self.cast_button.config(state='disabled')
        self.buy_gear_button.config(state='disabled')
        self.buy_bait_button.config(state='disabled')

    def _enable_controls(self):
        self.gear_combo.config(state='readonly')
        self.bait_combo.config(state='readonly')
        self.cast_button.config(state='normal')
        self.buy_gear_button.config(state='normal')
        self.buy_bait_button.config(state='normal')

    def buy_gear(self):
        try:
            index = self.gear_combo.current()
            if index >= 0:
                self.player.buy(index)
                self.update_displays()
                self.gear_combo.set(f"{self.player.fishing_gear_purchase.product.__class__.__name__} (${self.player.fishing_gear_purchase.price:.2f})")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def buy_bait(self):
        index = self.bait_combo.current()
        if index >= 0:
            self.player.buy_bait(index)
            self.update_displays()
            self.bait_combo.set(f"{self.player.bait_purchase.product.__class__.__name__} (${self.player.bait_purchase.price:.2f})")

    def cast(self):
        self._disable_controls()
        self.result_var.set("Waiting for Fish...")
        self.root.update()
        catch = self.player.cast()
        self.player.money += catch.to_money()
        self.update_displays()
        formatted_contents = [
            f"{fish}: {amount}"
            for fish, amount in catch.contents.items()
            if fish != "nothing"
        ]

        if not formatted_contents:
            msg = random.choice([
                "You didn't catch anything. Too Bad.",
                "You caught nothing. Better luck next time!",
                "Nothing on the line. Try again!",
            ])
        elif len(formatted_contents) == 1:
            msg = f"You caught a {list(catch.contents.keys())[0]}."
        else:
            msg = f"You caught:\n{'\n'.join(formatted_contents)}"
        self.result_var.set(msg)
        self._enable_controls()

if __name__ == "__main__":
    root = tk.Tk()
    app = FishingGame(root)
    root.mainloop()