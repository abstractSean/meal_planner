#!/usr/bin/env python3
"""Foods 

- Contains Food classes and subclasses
- Maintains food database.
- Tracks overall food consumption, real & planned.
- Different food classes, general to more specific.

Usage:
    Import food classes as needed.
"""

import sys
#  import os
#  import math

from pprint import pprint as pp
# insert function definitions here


class Food:
    """Store food superclass properties. Only name is required.
    Implement subclass template methods.

    Attributes:
        name (str): name of food
        amount (float): amount in units
        calories (int): calories / unit
        expiration_date (date?): date this food will expire
        group (str): 'carb', 'fat', 'fruit', 'protein', 'veg', 'fiber',
                     'seasoning', 
        health (int): scale of 1-10, 10 as healthiest, default 5.0
        pairings (:obj:`set` of Food): set of Food objects that pair well
        perishable (bool): True or False
        preptime (int): preptime in minutes
        price (float): total price/amount
        unit (str): 'gal', 'lb','oz', 'box', etc
        unit_price (float): unit price is in $/unit          
    """

    def __init__(self, name, amount=1.0, calories=0, expiration_date=None,
                 group='', health=5, pairings=(), perishable=False, preptime=0, 
                 price=0.0, unit='', unit_price=0.0):

        self.name = str(name)        
        self.amount = amount
        self.calories = calories
        self.expiration_date = expiration_date
        self.group = group
        self.health = health
        self.pairings = pairings
        self.perishable = perishable
        self.preptime = preptime
        self.price = price
        self.unit = unit
        self.unit_price = unit_price
        
        if self.unit_price == 0.0:
            self.calc_unit_price()
        if self.price == 0.0:
            self.calc_total_price()
            
    def __str__(self):
        return str(self.__dict__)
            
    def __repr__(self):
        return '{} object for "{}"'. format(type(self).__name__, self.name)

    def calc_unit_price(self):
        """Calculates unit_price = price / amount
        """
        self.unit_price = self.price / self.amount
        return self.unit_price

    def calc_total_price(self):
        """Calculates price = amount * unit_price
        """
        self.price = self.amount * self.unit_price
        return self.price


def main():
    """Contains module specific script for temporary testing.

    Args:
        args (type): describe arguments

    Returns:
        describe returns
    """

    # -------------------------
    # insert main run code here
    # execute automatic code
    # set variables to make available outside module
    # run scripting functions
    # -------------------------


if __name__ == '__main__':
    main() 
else:
    print("foods loaded.")
