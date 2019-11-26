# 1. Ham khong co tham so
def Hello():
    print("Hello Nguyen Duc Hung")

Hello()


# 2. Ham co ham so
def Sum(a,b,c):
    return a+b+c

print("Sum = ", Sum(1,2,3))


# 3. Ham co tham so mac dinh
# Chu y: phai dat tham so mac dinh tu Phai sang Trai
def SumS(a, b=1, c=2):
    return a+b+c

print("Sum = ", SumS(3))

'''
4. More about Farameter Function
'''
def Tong (*data): # truyen du lieu chua biet trc so luong
    t = 0
    for item in data:
        t = t + item
    return t

ketqua = Tong(10,20,30,40,50)
print("Ket qua = ", ketqua)

def TongS (*data):
    kq = []
    for item in data:
        tong = 0
        for n in item:
            tong = tong + n
        kq.append(tong)
    return kq

tong = TongS([1,2,3], [4,5,6])
print("Ket qua = ", tong,"\n\n")




def DienThoai (**data):
    count = 0
    for name,price in data.items():
        row = "{:10}{:10}".format(name,price)
        print(row)
        count = count + price
    return count

total = DienThoai(iphone=1000, samsung=2000, oppo=3000)
print("-"*20)
print("{:10}{:10}".format("Toal: ",total))

def TinhTong(n1,n2,n3, *data, **list):  #  ** dung cho dictionary
    sum1 = sum2 = sum3 =0
    sum1 = n1 + n2 + n3
    for item in data:
        sum2 = sum2 + item
    for key,value in list.items():
        sum3 = sum3 + value
    sum = [sum1, sum2, sum3]
    return sum

print("\n\n")
print(TinhTong(1,2,3, 4,5,6,7,8, one=10, two=20, three=30))
          # |n1,n2,n3|  data    |  list                   |



'''
5. Generator Function:  Hàm sinh ra

'''

r = range(0,5,1)
for i in r:
    print(i)


# Ham do coder viet

def myRange(start, length, step):
    i = start
    while (i<length):
        yield i
        i = i + 1

for item in myRange(0,5,1):
    print(item)

'''
=== Note ===

yeild: Hàm sẽ trả ra giá trị giống như return nhưng chương trình vẫn chạy tiếp
return: Hàm sẽ ngừng khi gặp return, trả vể giá trị của return

'''


# Viêt hàm Range()
def myRange(*thamso):
    start = length = step = 0
    if len(thamso)==3:
        start = thamso[0]
        length = thamso[1]
        step = thamso[2]
    elif len(thamso)==2:
        start = thamso[0]
        length = thamso[1]
    else:
        start = 0
        length = thamso[0]
        step = 1
    i = start
    while i<length:
        yield i
        i = i + step

print("\n\n")
myR = myRange(0,3,1)
print(list(myR))