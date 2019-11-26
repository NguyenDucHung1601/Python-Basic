'''
Bai 42: Viet 1 chuong trinh tao 1 tuple khac,
chua cac gtri la so chan trong tuple(1,2,3,4,5,6,7,8,9,10)
'''


def MakeOtherTuple(*data):
    data = tuple(data)
    l = []
    for item in data:
        if item % 2 == 0:
            l.append(item)
    print(tuple(l))


MakeOtherTuple(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
