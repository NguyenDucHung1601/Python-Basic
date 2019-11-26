'''
Bai 5: Nhap vao tu ban phim 1 chuoi so, phan cach nhau bang dau phay
Tao ra 1 list va 1 tuple chua moi so

'''

s = input("Nhap vao 1 chuoi so (cac so phan cach nhau boi dau phay):\n")
s = s.split(',')

T = list(s)
L = tuple(s)

print("List : ", L)
print("Tuple: ", T)
