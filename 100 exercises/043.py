'''
Bai 43: Viet chuong trinh de tao ra va in tuple chua cac so chan
duoc lay tu tuple(1,2,3,4,5,6,7,8,9,10)
'''


def MakeNewTuple(*data):
    data = tuple(data)
    l = []
    for item in data:
        if item % 2 == 0:
            l.append(item)
    print(tuple(l))


MakeNewTuple(1,2,3,4,5,6,7,8,9,10)