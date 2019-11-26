'''
a = 100
b = 0
x = a/b
# ZeroDivisionError
'''

try:
    a = 100
    b = 0
    x = a/b
except:
    print("Số b phải khác 0")


# Hay hơn:
try:
    a = 100
    b = 0
    x = a/b
except ZeroDivisionError as error:
    print("Lỗi: ", error)

