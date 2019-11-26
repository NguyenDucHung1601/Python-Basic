'''
Bai 33: Dinh nghia 1 ham co the in dictionary chua cac key la so dem tu 1 den 20
va cac gtri binh phuong cua chung
'''


def Dictionary(n):
    dicitonary = {}
    for i in range(1, n + 1):
        dicitonary[i] = i ** 2
    print(dicitonary)


Dictionary(20)
