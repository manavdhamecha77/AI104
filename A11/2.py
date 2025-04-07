"""
Write a Pandas program to convert all the string values to upper, lower cases in a given
pandas series. Also find the length of the string values.
s = pd.Series (['X', 'Y', 'T', 'Aaba', 'Baca', 'CABA', None, 'bird', 'horse', 'dog'])
"""

import pandas as pd

s = pd.Series(['X', 'Y', 'T', 'Aaba', 'Baca', 'CABA', None, 'bird', 'horse', 'dog'])

upper_case = s.str.upper()
print("Upper case:\n", upper_case)

lower_case = s.str.lower()
print("\nLower case:\n", lower_case)

string_lengths = s.str.len()
print("\nString lengths:\n", string_lengths)
