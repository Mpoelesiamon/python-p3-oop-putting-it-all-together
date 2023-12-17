#!/usr/bin/env python3

class Book:
    def __init__(self, title, pages, price):
        if not isinstance(pages, int):
            raise ValueError("page_count must be an integer")
        self.title = title
        self.pages = pages
        self.price = price
        self.discount = 0

    def set_discount(self, amount):
        if 0 <= amount <= 100:
            self.discount = amount
        else:
            raise ValueError("Discount must be between 0 and 100.")

    def discounted_price(self):
        return self.price * (1 - self.discount / 100)

    def turn_page(self):
        return "Flipping the page...wow, you read fast!"

        