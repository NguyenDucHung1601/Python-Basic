'''
Interator : Truy xuất phần tử trong List, String

'''

list = [1,2,3,4,5]
I = iter(list)
print(type(I))

print(I.__next__())   # 1
print(I.__next__())   # 2
print(I.__next__())   # 3
print(I.__next__())   # 4
print(I.__next__())   # 5


