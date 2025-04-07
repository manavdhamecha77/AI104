"""
After accidentally leaving an ice chest of fish and shrimp in your car for a week while you
were on vacation, you're now in the market for a new vehicle. Your insurance didn't cover
the loss, so you want to make sure you get a good deal on your new car.
Given a Series of car asking_prices and another Series of car fair_prices, determine which
cars for sale are a good deal. In other words, identify cars whose asking price is less than
their fair price.
The result should be a list of integer indices corresponding to the good deals
in asking_prices.
"""

import pandas as pd

asking_prices = pd.Series([12000, 15000, 17000, 11000, 13500])
fair_prices = pd.Series([13000, 14000, 17500, 11500, 13000])

# Find indices where asking price is less than fair price
good_deals = asking_prices[asking_prices < fair_prices].index.tolist()

print("Good deal indices:", good_deals)
