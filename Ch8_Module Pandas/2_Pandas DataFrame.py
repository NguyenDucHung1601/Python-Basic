import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from numpy.random import randn

df1 = pd.read_clipboard()
print(df1)

print(df1.columns)
print(df1.head())
print(df1.tail())
print(df1.Exchange) # Lay cot du lieu theo ten cot
df1.Exchange = 'Down 1' # Thay doi cot du lieu