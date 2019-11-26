# s = {1,2,3,4,5}  # set không có sắn index
# a,b,c,d,e = s    # gắn index cho set
# # print(c)
#
# for item in s:
#     print(item)



'''

set('aaabbbbcccc')       # ('a', 'b', 'c')  tự sắp xêp theo thứ tự tăng dần
A,B         # {{},{}}
A-B         # Loại bỏ những phần tử trong set A mà set B có
A|B         # Gộp 2 set lại với nhau và loại bỏ phần tử set A đã có
A&B         # Giữ giá trị mà cả 2 set có
A^B         # Gộp 2 set lại với nhau Loại bỏ những phần tử trong set A mà set B có

'''


A = {1,2,3,4}
B = {3,4,5,6}

C1 = (A,B)
print("C1:    ", C1)

C2 = (A-B)
print("C2:    ", C2)

C3 = (A|B)
print("C3:    ", C3)

C4 = (A&B)
print("C4:    ", C4)

C5 = (A^B)
print("C5:    ", C5)