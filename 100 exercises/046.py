'''
Bai 46: Viet chuong trinh dung map() de tao list
chua cac gtri binh phuong cua cac so trong [1,2,3,4,5,6,7,8,9,10]

* Su dung map() de tao list
* Su dung lamba() de dinh nghia ham chua biet
'''

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squareNumners = list(map(lambda x: x ** 2, li))
print(squareNumners)
