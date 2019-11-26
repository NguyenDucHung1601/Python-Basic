'''
Bai 45: Viet chuong trinh co the loc cac so chan trong danh sach
su dung ham filter. Danh sach la [1,2,3,4,5,6,7,8,9,10]

* Su dung filter() de loc cac yeu to trong 1 list
* Su dung lamba() de dinh nghia cac ham chua biet

'''

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evenNumber = list(filter(lambda x: x % 2 == 0, li))
print(evenNumber)
