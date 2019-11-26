'''
Bai 3: Voi so nguyen n, tao dictionary chua (i, i*i) nhu la 1 so nguyen dem tu 1 den n

'''

dictionary = {}
n = int(input("Nhap so nguyen n: "))

for i in range(1, n + 1):
    dictionary[i] = i * i

print(dictionary)
