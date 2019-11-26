'''
Bai 20: Tinh so tien thuc cua 1 tai khoan ngan hang dua tren nhat ki giao dich nhap tu ban phim
Dinh dang nhat ki hien thi nhu sau
D: tien gui
W: tien rut ra
'''

diary = ""
s = input("Nhap nhat ki giao dich (D tiengui / W tienrut):  ")
while len(s) != 0:
    diary = diary + s + "\n"
    s = input("Nhap nhat ki giao dich (D tiengui / W tienrut):  ")

diary.rstrip("\n")
print("\n== Nhat ki giao dich ==")
print(diary)
diary = diary.splitlines()
money = 0
for item in diary:
    if item[0] == "w":
        item = int(item.lstrip("w").lstrip("W").lstrip())
        money -= item
    elif item[0] == "d":
        item = int(item.lstrip("d").lstrip("D").lstrip())
        money += item

print("Tong tien trong ngan hang: ", money)
