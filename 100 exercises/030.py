'''
Bai 30: Dinh nghia 1 ham co input 2 chuoi
In ra chuoi co do dai lon hon
Neu 2 chuoi dai bang nhau thi in ca 2 chuoi theo dong
'''


def CompareString(str1, str2):
    if len(str1) > len(str2):
        print(str1)
    elif len(str2) > len(str1):
        print(str2)
    else:
        print(str1)
        print(str2)


s1 = input("Nhap chuoi thu nhat: ")
s2 = input("Nhap chuoi thu hai : ")
CompareString(s1, s2)
