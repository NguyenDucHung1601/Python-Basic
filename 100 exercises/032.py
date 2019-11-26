'''
Bai 32: Dinh nghia 1 ham co the in dictionary chua key la cac so tu 1 den 3
va cac gtri binh phuong cua chung
'''


def Dictionary(n):
    dictionary = {}
    for i in range(1, n + 1):
        dictionary[i] = i ** 2
    print(dictionary)


Dictionary(3)
