'''
Bai 16: Nhap vao 1 cau, dem so chu cai va so chu so trong cau do
'''

numNumber = 0
numCharacter = 0

s = input("Nhap vao 1 cau:\n")

i = 0
while i < len(s):
    if s[i].isdigit():
        numNumber += 1
    else:
        if s[i].isalpha():
            numCharacter += 1
    i += 1

print("So chu cai: ", numCharacter)
print("So chu so : ", numNumber)
