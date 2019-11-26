import numpy as np

'''
Co the tao array tu list roi chuyen kieu sang array
Co the tao truc tiep array
Co the gop nhieu array thanh 1 array


'''

a = [1, 2, 3, 4, 5]  # list
b = [6, 7, 8, 9, 10]
c = [11, 12, 13, 14, 15]
''' === chuyen kieu list thanh Array === '''
arr1 = np.array(a)  # chuyen sang kieu array
arr2 = np.array(b)
arr3 = np.array(c)

print(type(arr1))
print(arr1,"\n")

''' === Gop cac array thanh 1 array === '''
tongArray = np.array([arr1, arr2, arr3])
print(tongArray)

''' === Hien thi hang-cot cua array nhieu chieu === (array 1 chieu khong dung dc) '''
print(tongArray.shape) # 3 dong 5 cot --> mang da chieu
print()

''' === Dat lai so hang-cot cho array nhieu chieu === (array 1 chieu khong dung dc)'''
tongArray.reshape(5,3) # doi lai hinh 5 hang 3 cot
print(tongArray.reshape(5,3))
print()

''' === Xay dung Array truc tiep === '''
A = np.arange(10) # su dung tuong tu nhu ham range()
print(A)

B = np.arange(5,50,3) # su dung tuong tu nhu ham range()
print(B)
print()

Hung = np.array([1,2,3,4,5])
print(Hung)
print()

''' === Tao mang dac biet cac phan tu giong nhau === '''
print(np.zeros(5))
print(np.ones(5))
print(np.empty(5))

''' Xem them: docs.scipy.org '''
