#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size, price):
        if not isinstance(size, int):
            raise ValueError("size must be an integer")
        self.brand = brand
        self.size = size
        self.price = price
        self.discount = 0
        self.condition = "New"

    def set_discount(self, amount):
        if 0 <= amount <= 100:
            self.discount = amount
        else:
            raise ValueError("Discount must be between 0 and 100.")

    @property
    def discounted_price(self):
        return self.price * (1 - self.discount / 100)

    def cobble(self):
        self.condition = "New"

    def repair(self):
        return "The shoe has been repaired."
