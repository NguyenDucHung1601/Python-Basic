'''
Bai 15: Tim tat ca cac so trong doan [1000,3000],
sao cho tat ca cac chu so trong do deu la so chan.
In cac so tim duoc thanh chuoi phan cach nhau boi dau phay.
'''

nums = []
for i in range(1000, 3001):
    s = str(i)
    if (int(s[0]) % 2 == 0) and (int(s[1]) % 2 == 0) and (int(s[2]) % 2 == 0) and (int(s[3]) % 2 == 0):
        nums.append(s)

print(",".join(nums))
