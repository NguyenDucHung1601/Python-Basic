'''
Bai 44: Viet chuong trinh nhap 1 chuoi vao
In "Yes" neu chuoi la "Yes" hoac "YES" hoac "yes"
In "No" neu chuoi la "No" hoac "NO" hoac "no"
'''


def YesOrNo():
    s = input("Nhap vao: ")
    if (s == "Yes") or (s == "YES") or (s == "yes"):
        print("Yes")
    elif (s == "No") or (s == "NO") or (s == "no"):
        print("No")


YesOrNo()
