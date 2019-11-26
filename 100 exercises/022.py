'''
Bai 22: Viet chuong trinh sap xep tuple(name,age,score) theo thu tu tang dan
Tuple duoc nhap vao boi nguoi dung
Tieu chi sap xep la: Name > Age > Score

Note: Su dung itemgetter de chap nhan key sap xep
'''
from operator import itemgetter

l = []
s = input("Enter info (Name,Age,Score): ")
while (len(s) != 0):
    l.append(tuple(s.split(',')))
    s = input("Enter info (Name,Age,Score): ")

print(l.sort(key=itemgetter(0, 1, 2)))
