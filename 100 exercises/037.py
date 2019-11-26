'''
Bai 37: Dinh nghia 1 ham co the tao list chua cac gtri binh phuong cua cac so tu 1 den 20
In 5 muc dau tien trong list
'''


def List(n):
    l = []
    for i in range(1, n + 1):
        l.append(i ** 2)
    print(l[:5])

List(20)
