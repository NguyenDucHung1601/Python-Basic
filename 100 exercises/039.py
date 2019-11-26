'''
Bai 39: Dinh nghia 1 ham co the tao ra list chua cac gtri binh phuong
cua cac so tu 1 den 20. In ra tat cac cac gtri cua list, tru 5 muc dau tien
'''


def List(n):
    l = []
    for i in range(1, n + 1):
        l.append(i ** 2)
    print(l[5:])


List(20)
