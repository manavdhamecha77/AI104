"""
Write a Pandas program to create
a) Date time object for Jan 15 2012.
b) Specific date and time of 9:20 pm.
c) Local date and time.
d) A date without time.
e) Current date.
t) Time from a date time.
g) Current local time.
"""

import pandas as pd
from datetime import datetime

# a) Date time object for Jan 15 2012
dt_a = pd.Timestamp('2012-01-15')
print("a)", dt_a)

# b) Specific date and time of 9:20 PM
dt_b = pd.Timestamp('2012-01-15 21:20')
print("b)", dt_b)

# c) Local date and time (now)
dt_c = pd.Timestamp.now()
print("c)", dt_c)

# d) A date without time
dt_d = pd.Timestamp('2024-04-07').date()
print("d)", dt_d)

# e) Current date
dt_e = pd.Timestamp.today().date()
print("e)", dt_e)

# t) Time from a date time
dt_t = pd.Timestamp.now().time()
print("t)", dt_t)

# g) Current local time
dt_g = datetime.now().time()
print("g)", dt_g)
