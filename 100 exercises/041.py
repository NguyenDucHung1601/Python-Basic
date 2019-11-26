'''
Bai 41: Voi tuple (1,2,3,4,5,6,7,8,9,10)
Viet chuong trinh in 1 nua so gtri dau tren 1 dong
                     1 nua so gtri cuoi tren 1 dong
'''


def PrintHalfHalfTuple(n):
    l = []
    for i in range(1, n + 1):
        l.append(i)
    t = tuple(l)
    print(t[:int(len(t) / 2)])
    print(t[int(len(t) / 2):])


PrintHalfHalfTuple(10)
