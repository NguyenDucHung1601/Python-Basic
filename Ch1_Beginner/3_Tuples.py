'''
t = (1,2,3)

t[index]    # Lấy phần tử tại vtri index
t = t + t   # Cộng dồn tuple
t[from:to]  # Trích xuất tuple từ vtri from -> to
T = (t,l)   # Gộp tuples con và list con

'''

t1 = (1,2,3)
t2 = (4,5,6)
l1 = ["A", "B", "C"]

T = t1 + t2
T = (t1,t2)
print(T)

T = (t1,l1)
print(T)