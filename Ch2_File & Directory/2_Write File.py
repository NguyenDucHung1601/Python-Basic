# fp = open("data/list2.txt","w")
# fp.write("Nguyen Duc Hung\n")
# # fp.write("\n")
# fp.write("Hoc vien Ky thuat quan su\n")
# # fp.write("\n")
# print("Done")

rFile = open("data/list.txt","r")
wFile = open("data/list2.txt","w")
for line in rFile:
    wFile.write(line)
print("Done")
