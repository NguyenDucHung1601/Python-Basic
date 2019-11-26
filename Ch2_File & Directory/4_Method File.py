'''
f = open("data/data1.txt","r")

data = f.read()     # Đọc dữ liệu từ file
print(len(data))    # Độ lớn của dữ liệu
f.tell()            # Đọc đến vị trí nào rồi?
f.seek(100)         # Di chuyển con trỏ đọc file

'''


# 1_________________________________________________
f = open("data/data1.txt","r")

fops = f.tell()
print("== Đọc tới vị trí ", fops, " ==")

line = f.readline()
print(line, end = "")
fpos = f.tell()
print("== Đọc tới vị trí ", fops, " ==")

line = f.readline()
print(line, end = "")
fpos = f.tell()
print("== Đọc tới vị trí ", fops, " ==")

line = f.readline()
print(line, end = "")
fpos = f.tell()
print("== Đọc tới vị trí ", fops, " ==")


# 2____________________________________________________
f = open("data/data1.txt", "r")

fops = f.tell()
print("Đọc tới vị trí ", fops)

f.seek(300)
print("-"*50)

data = f.read()
print(len(data))

