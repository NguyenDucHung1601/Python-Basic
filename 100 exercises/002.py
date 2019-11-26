'''
Bai 2: Tnh giai thua cua 1 so cho truoc
'''


def Fact(n):
    if n == 0:
        return 1
    else:
        fact = 1
        i = 1
        for i in range(1, n + 1):
            fact = fact * i
            i = i + 1
        return fact


num = int(input("Nhap so can tinh giai thua: "))
print(num, "! = ", Fact(num))