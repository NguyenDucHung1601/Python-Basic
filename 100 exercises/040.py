'''
Bai 40: Dinh nghia 1 ham co the tao va in ra 1 tuple chua cac gtri
binh phuong cua cac so tu 1 den 20
'''


def Tuple(n):
    l = []
    for i in range(1, n + 1):
        l.append(i ** 2)
    t = tuple(l)
    print(t)


Tuple(20)
