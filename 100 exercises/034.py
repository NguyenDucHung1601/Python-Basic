'''
Bai 34: Dinh nghia 1 ham co the tao dictionay, chua cac key la cac so tu 1 den 20
va cac gtri binh phuong cua chung. ham chi in ra cac gtri
'''


def Dictionary(n):
    dictionary = {}
    for i in range(1, n + 1):
        dictionary[i] = i ** 2
    print(dictionary.values())


Dictionary(20)
