'''

Sử dụng buffer để đọc ghi file hiệu quả hơn
dùng đối với file lớn, tránh lỗi

'''

BUFFERSIZE = 100000 # lỗi lần đọc 100000 byte
rFile = open("data/data1.txt","r")
wFile = open("data/data2.txt","w")

buffer = rFile.read(BUFFERSIZE)

i=0
while(len(buffer)):
    i = i + 1
    wFile.write(buffer)
    print(i,"{} byte".format(len(buffer)))
    buffer = rFile.read(BUFFERSIZE)
print("Done")
