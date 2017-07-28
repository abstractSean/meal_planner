#!/usr/bin/env python3
"""Insert module docstring here

Usage:
    Describe usage here
"""

import sys
from datetime import datetime as dt
from datetime import timedelta
#  import os
#  import math
from recipes import Recipe
#  from ** * import ** *
#  add imported modules/functions from modules


# insert function definitions here
class MealPlan:
    def __init__(self, start_date, end_date, length):
        self.start_date = start_date
        if end_date:
            self.end_date = end_date
        elif length:
            self.end_date = start_date + timedelta(length)

def main():
    """Insert docstring for main function here

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
    print("Module Loaded message")
