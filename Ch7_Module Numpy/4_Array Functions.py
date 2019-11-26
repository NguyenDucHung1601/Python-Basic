import numpy as np

''' Sinh so ngau nhien trong khoang [1,10] '''
x = np.random.randint(1, 10)
print(x,"\n")

# Tao mang 2 chieu [x][y] tu 2 list x,y
x = []
y = []
for i in range(10):
    x.append(np.random.randint(1, 10))
    y.append(np.random.randint(1, 10))
print(x,y)

x = np.array(x)
y = np.array(y)
print(x,y,"\n")

''' ===( Thao tac ten 2 mang voi cac phan tu tuong ung )=== '''

'''  a[i] = x[i] + y[i]  '''
print(np.add(x,y),"\n") # Cong gop 2 mang thanh 1 mang (cac ptu tuong ung cong vs nhau )

'''  a[i] = max(x[i],y[i]  '''
print(np.maximum(x,y),"\n") # So sanh cac ptu tuong ung cua 2 mang, chon ra ptu lon nhat

'''  a[i] = min(x[i],y[i])  '''
print(np.minimum(x,y),"\n") # So sanh cac ptu tuong ung cua 2 mang, chon ra phan tu nho nhat

'''  a[i] = sqrt(x[i])  '''
print(np.sqrt(x),"\n")  # Can bac 2 cac ptu trong x

'''  a[i] = x[i]^2  '''
print(np.square(x),"\n")  # Binh phunog cac ptu trong x

'''  a[i] = x[i]/y[i]  '''
print(np.divide(x,y),"\n")  # Lay ptu cua x chia tuong ung cho cac ptu cua y

'''  a[i] = x[i]^y[i]  '''
print(np.power(x,y),"\n")  # x[i] = x[i] ^ y[i]

''' Sap xep mang x '''
print(np.sort(x),"\n")

''' Loai bo cac ptu trung nhau cua mang x '''
print(np.unique(x),"\n")

''' Ktra x[i] > y[i]  tra ve mang tuong ung voi cac ptu True hoac False '''
print(np.greater(x,y),"\n")

b = np.greater(x,y)
print(b.all())  # hoac print(np.all(b)) -- Ktra b, neu co 1 cai False ---> tra ve False '''
print(b.any())  # hoac print(np.any(b)) -- Ktra b, neu co 1 cai True ---> tra ve True '''

''' Ktra x[i] = y[i]  tra ve mang tuong ung voi cac ptu True False '''
print(np.equal(x,y),"\n")

'''

TÌM HIỂU THÊM TRÊN GOOGLE:  python numpy functions

'''