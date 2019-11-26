'''
Bai 10: Nhap vao X,Y
Tao mang 2 chieu, gtri ptu (i,j) la i*j

'''

x = int(input("Nhap X: "))
y = int(input("Nhap Y: "))

for i in range(x):
    for j in range(y):
        print(i*j, end = " ")
    print()
