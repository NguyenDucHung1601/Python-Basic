'''
Bai 52: Dinh nghia 1 class co ten la Circle
co the nhap tu ban phim
co phuong thuc tinh dien tich
'''


class Circle:
    r = 0

    def __init__(self, r):
        self.r = r

    def BanKinh(self):
        self.r = float(input("Nhap ban kinh: "))

    def DienTich(self):
        return 3.14 * (self.r) ** 2


c = Circle(2)
print(c.DienTich())
