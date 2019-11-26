'''
Bai 5: Dinh nghia 1 class co it nhat 2 method:
getString: nhan 1 chuoi do nguoi dung nhap vao tu ban phim
printString: in chuoi vua nhap sang chu hoa
'''


class String:
    s = ""

    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input("Nhap vao 1 chuoi:\n")

    def printString(self):
        print("Chuoi nhap vao: ", self.s)
        print("Chuoi chu hoa : ", self.s.upper())


str = String()
str.getString()
str.printString()
