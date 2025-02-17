import pandas as pd
import numpy as np
from collections import Counter

def count_two(nums: list):
    return Counter(nums)[2]

df = pd.DataFrame({'coll': [1, 3, 5],
                    'col2': [2, 4, 6]})
print(df.agg(['sum', count_two]))