'''
Bai 51: Dinh nghia 1 class VietNam
co class con la HaNoi
'''


class VietNam:
    def print(self):
        print("Viet Nam")


class HaNoi(VietNam):
    def print(self):
        print("Ha Noi")


vn = VietNam()
hn = HaNoi()
vn.print()
hn.print()
