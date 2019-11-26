'''
Bai 36: Dinh nghia 1 ham co the tao va in list cua cac gtri binh phuong cua cac so tu 1 den 20
'''


def List(n):
    l = []
    for i in range(1, n + 1):
        l.append(i ** 2)
    print(l)


List(20)
