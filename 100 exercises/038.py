'''
Bai 38: Dinh nghia 1 ham co the tao ra list chua cac gtri binh phuong
cua cac so tu 1 den 20. In ra 5 gtri cuoi cung cua list
'''


def List(n):
    l = []
    for i in range(1, n + 1):
        l.append(i ** 2)
    print(l[-5:])


List(20)
