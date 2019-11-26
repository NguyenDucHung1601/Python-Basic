'''
Bai 13: Nhap 1 chuoi tu ban phim, cac tu tach biet boi khoang trang
Loai bo cac tu trung lap, sap xep theo thu tu bang chu cai roi in ra

su dung ham set(words): loai bo du lieu trung
su dung ham sorted(words): Sap xep du lieu

'''

s = input("Nhap vao 1 chuoi, cac tu phan cach nhau boi khoang trang:\n")

words = list(s.split())
words = set(words)
words = sorted(words)
print(words)
