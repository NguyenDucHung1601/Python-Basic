'''
Array Slices Are Views: Vấn đề cắt mảng

'''

import numpy as np

A = np.arange(20)
print(A, "\n")
a1 = A[:10]  # a1 cat tu A, lay 10 ptu dau tien --> a1 la con cua A
print(a1, "\n")
a1[:] = 100  # Dat gtri tat cac ptu cua a1 thanh 100
print(a1, "\n")
print(A, "\n")  # A da bi thay doi phan cat cho a1
B = A.copy()  # B la ban sao cua A
print(B, "\n")
print(B[0])  # phan tu B[0]
B[0] = 5000  # doi gtri phan tu B[0]
print(B[0])
print("\n\n")

''' Ngoai ra co the cat list '''
x = list(range(20))  # list x
print(x)
y = x[:10]  # y la list cat tu x
print(y)
y[0] = 100  # doi gtri ptu y[0] cua list y
print(y)
print(x)  # list x van khong vi thay doi
print("\n\n")

''' === Cat mang da chieu === '''

A = np.arange(25).reshape(5, 5)
print(A, "\n")
print(A[2:5],"\n")     # Hien thi khoang hang
print(A[2:5, 1:4],"\n") # Hien thi khoanh hang va cot
print(A[[1,2,4]],"\n")  # Hien thi cac hang

print(A.sum())  # Tong cac phan tu cua A
