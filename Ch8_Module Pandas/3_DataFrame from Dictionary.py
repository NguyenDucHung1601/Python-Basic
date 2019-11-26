import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from numpy.random import randn

diem = [10,9,8,7]
sinhvien = ["Anh","Bao","Cong","Dung"]

data = {'diem': diem, 'sinhvien': sinhvien}
print(data)

df = DataFrame(data)
print(df)

ind = "A B C D E".split()
cols = "col1 col2 col3 col4 col5".split()
x = []
for i in range(25):
    x.append(np.random.randint(1,100))

x = np.array(x)
x = x.reshape(5,5)
print(x)

df2 = DataFrame(x, index=ind, columns=cols)
print(df2)

new_ind = "A B C D E F G H I K".split()
df3 = df2.reindex(new_ind,fill_value=0)
print(df3)

new_cols = "col1 col2 col3 col4 col5 col6 col7 col8".split()
df4 = df2.reindex(columns = new_cols, fill_value=0)
print(df4)