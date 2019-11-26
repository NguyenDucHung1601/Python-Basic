'''
Bai 18: Nhap vao 1 so a
Tinh gia tri a + aa + aaa + aaaa
'''

a = int(input("Nhap vao a: "))

n4 = a * 1000 + a * 100 + a * 10 + a
n3 = a * 100 + a * 10 + a
n2 = a * 10 + a

print("A = a + aa + aaa + aaaa = ", a + n2 + n3 + n4)
