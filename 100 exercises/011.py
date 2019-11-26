'''
Bai 11: Nhap 1 chuoi tu ban phim, cac tu phan tach nhau boi dau phay.
In nhung tu do tho thu tu bang chu cai, phan tach nhau boi dau phay.
'''

s = input("Nhap vao 1 chuoi, (cac tu phan cach nhau boi dau phay):\n")
words = list(s.split(','))
words.sort()
print(",".join(words))
