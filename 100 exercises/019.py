'''
Bai 19: Nhap vao 1 danh sach, loc ra cac so le
'''

s = input("Nhap vao 1 danh sach cac so (phan cach nhau boi dau phay):\n")
List = list(s.split(','))

List2 = []
for i in List:
    if int(i) % 2 != 0:
        List2.append(i)

print("Danh sach cac so le: ", List2)

