'''
Bai 12: Viet chuong trinh chap nhan chuoi la cac dong duoc nhap vao
Chuyen cac dong nay thanh chu in hoa va in ra man hinh
'''

print("Nhap chuoi:")
lines = []

str = ""
s = input()
while len(s)!=0:
    str = str + s + "\n"
    s = input()


print(str.upper())

