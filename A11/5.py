"""
Given a dataset of concerts, count the number of concerts per (artist, venue), per year
month. Make the resulting table be a wide table - one row per year month with a column
for each unique (artist, venue) pair. Use the cross product of the artists and venues Series
to determine which (artist, venue) pairs to include in the result.
"""

import pandas as pd
import itertools

data = {
    'artist': ['A', 'B', 'A', 'A', 'B', 'C'],
    'venue': ['X', 'Y', 'X', 'Y', 'Y', 'Z'],
    'date': pd.to_datetime(['2024-01-10', '2024-01-15', '2024-02-20', 
                            '2024-01-22', '2024-02-10', '2024-02-11'])
}
concerts = pd.DataFrame(data)

artists = pd.Series(['A', 'B', 'C'])
venues = pd.Series(['X', 'Y', 'Z'])

concerts['year_month'] = concerts['date'].dt.to_period('M')

grouped = concerts.groupby(['year_month', 'artist', 'venue']).size().reset_index(name='count')

all_combinations = pd.MultiIndex.from_product(
    [concerts['year_month'].unique(), artists, venues],
    names=['year_month', 'artist', 'venue']
)

full_df = grouped.set_index(['year_month', 'artist', 'venue']).reindex(all_combinations, fill_value=0).reset_index()

wide_table = full_df.pivot(index='year_month', columns=['artist', 'venue'], values='count')

wide_table.columns = [f"{a}_{v}" for a, v in wide_table.columns]
wide_table = wide_table.reset_index()

print(wide_table)
