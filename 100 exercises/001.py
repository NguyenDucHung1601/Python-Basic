'''
Bai 1: Tim tat ca cac so nam trong [2000,3200]
chia het cho 7 nhung khong phai boi cua 5
'''

list = []
for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        list.append(str(i))
print(','.join(list))
