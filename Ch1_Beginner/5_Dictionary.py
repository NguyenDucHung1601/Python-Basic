'''
d = {'key1':1, 'key2':2, 'key3':3}

len(d)             # Đếm số phần tử trong Dictionary
del d[index]       # Xoá 1 phần tử có key là index
d.keys()           # Lấy ra khoá của Dictionary
d.values()         # Lấy ra giá trị của Dictionary
d.items()          # Hiển thị đầy đủ key và value của Dictionary

'''


d = {'hs1': "Nguyen", 'hs2': "Duc", 'hs3': "Hung"}
print(len(d))
print(d.keys())
print(d.values())
print(d.items())

print(d['hs1'])

diem = dict(A=10 , B=9, C=8)  # Có thể định nghĩa list ntn
print(dict)


result = {x:x**2 for x in range(10)} # Tối ưu hoa code khi tạo dictionary
print(result)

d = {'name':'Nguyễn Đức Hưng', 'age':'21', 'university':'MTA'}
print(d)
d['age'] = 26
d.popitem() # Xoá item ngẫu nhiên trong dictionary
print(d)