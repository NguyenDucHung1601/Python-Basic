'''
Array Arthimetic : Phép toán trong Arry

'''

import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr, "\n")

print(arr + 10, "\n")  # Tat ca cac phan tu trong Array deu dc cong them 10
print(arr * arr, "\n")  # Tat cac cac phan tu trong Array deu dc nhan vs chinh no
print(arr ** 3, "\n")  # Tat cac cac phan tu trong Array deu duoc luy thua voi 3
print(arr - arr, "\n")  # Tat cac cac phan tu trong Array = 0

# Transpose (dao cot->dong; dong->cot)
A = np.arange(25).reshape(5,5)
print(A,"\n")
print(A.T,"\n") # Dao nguoc: cot -> dong;  dong -> cot