'''
Bai 17: Nhap vao 1 cau, dem so chu hoa, chu thuong
'''

numLower = 0
numUpper = 0

s = input("Nhap vao 1 cau:\n")

i = 0
while i < len(s):
    if s[i].islower():
        numLower += 1
    elif s[i].isupper():
        numUpper += 1
    i += 1

print("So chu hoa   : ", numUpper)
print("So chu thuong: ", numLower)