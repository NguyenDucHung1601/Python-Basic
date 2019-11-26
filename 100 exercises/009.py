'''
Bai 9: Tinh gia tri theo cong thuc Q = sqrt((2*C*D)/H)
voi C = const = 50
    H = const = 30
    D la gtri tuy bien, nhap vao tu ban phim, cac gtri D phan cach bang dau phay
'''

import math

values = input("Nhap vao cac gia tri cua D (phan cach nhau boi dau phay):\n")
values = values.split(',')
D = list(values)

C = 50
H = 30
i = 0
while i < len(D):
    D[i] = int(D[i])
    print("D =", D[i], "--> Q =", math.sqrt((2 * C * D[i]) / H))
    i += 1
