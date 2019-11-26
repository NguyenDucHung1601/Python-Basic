import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from numpy.random import randn

''' Tao Pandas series '''

# Tao truc tiep, index mac dinh la 0,1,2,3
S1 = Series([10, 20, 30, 40])
print(S1)

# Tao truc tiep, tu gan index
S2 = Series([10, 20, 30, 40], index=['A', 'B', 'C', 'D'])
print(S2)

# Tao thong qua 2 list
diem = [10, 9, 8, 7]
hocsinh = ["A", "B", "C", "D"]
S3 = Series(diem, index=hocsinh)
print(S3)

print(S3["A"])

# Chuyen series sang dictionary
s3d = S3.to_dict()
print(s3d)

# Chuyen dictionary sang series
S4 = Series(s3d)
print(S4)

# Ktra series null (tra ve kieu bool)
print(pd.isnull(S4))

# Them ten cho series
S4.name = "Danh sach"
print(S4)

# Ktra series not null (tra ve kieu bool)
print(pd.notnull(S4))

# Cong 2 series
print(S3+S4)

# Lay index va value cua series
print(S4.index)
print(S4.values)

# Reindex (dat lai index cho series)
x = list(range(10,15))
ind = ['a','b','c','d','e']
S5 = Series(x,ind)
print(S5)
ind2 = ['A','B','C','D','E','F','G','H']
S6 = S5.reindex(ind2,fill_value=0)
print(S6)

# Loc du lieu
print(S4)
print(S4[0])
print(S4[S4==10])
print(S4[S4>10])
print(S4[S4<10])
print(S4[S4>=9])

# Duyet va sap xep du lieu
S7 = Series([0,1,2], index=['A','B','C'])
S8 = Series([3,4,5,6],index=['A','B','C','D'])
print(S7+S8)

ind = "a b c d e f g h i j".split()
print(ind)
x = []
for i in range(10):
    x.append(np.random.randint(1,100))

S9 = Series(x,index=ind)
print(S9)