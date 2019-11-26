'''
Bai 35: Dinh nghia 1 ham co the tao dictionary chua key la cac so tu 1 den 20
va cac gtri binh phuong cua chung. ham chi can in ra cac key
'''


def Dictionary(n):
    dictionary = {}
    for i in range(1, n + 1):
        dictionary[i] = i ** 2
    print(dictionary.keys())


Dictionary(20)
