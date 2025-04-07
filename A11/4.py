"""
Whenever your friends John and Judy visit you together, y'all have a party. Given a
DataFrame with 10 rows representing the next 10 days of your schedule and whether John
and Judy are scheduled to make an appearance, insert a new column
called days_til_party that indicates how many days until the next party.
days_til_party should be 0 on days when a party occurs, 1 on days when a party doesn't
occur but will occur the next day, etc.
"""

import pandas as pd
import numpy as np

df = pd.DataFrame({
    'John': [True, False, True, False, True, True, False, False, True, False],
    'Judy': [True, True, False, True, False, True, False, True, True, False]
})

party_days = (df['John'] & df['Judy'])

days_til_party = [None] * len(df)
next_party = None

for i in reversed(range(len(df))):
    if party_days[i]:
        days_til_party[i] = 0
        next_party = 0
    elif next_party is not None:
        next_party += 1
        days_til_party[i] = next_party
    else:
        days_til_party[i] = np.nan  # No future party scheduled yet

df['days_til_party'] = days_til_party

print(df)
