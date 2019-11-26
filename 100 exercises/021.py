'''
Bai 21: Mot website yeu cau nguoi dung nhap Ten nguoi dung va Mat khau
Ktra tinh hop le cua Mat khau nhap vao
Cac tieu tri ktra mat khau bao gom:
1. It nhat 1 chu cai nam trong [a-z]
2. It nhat 1 chu cai nam trong [A-Z]
3. It nhat 1 chu so nam trong [0-9]
4. It nhat 1 ky tu nam trong [$#@]
5. Do dai password toi thieu: 6
6. Do dai password toi da: 12
'''


def checkPassword(pas):
    numNumber = numLower = numUpper = 0
    if (len(pas) < 6) or (len(pas) > 12):
        return False
    if (not ('$' in pas)) and (not ('#' in pas)) and (not (('@' in pas))):
        return False
    for i in pas:
        if 'a' <= int(pas[i]) <= 'z':
            numLower += 1
        if i in "[a-z]":

        if 'A' <= int(pas[i]) <= 'Z':
            numUpper += 1
        if 0 <= int(pas[i]) <= 9:
            numNumber += 1
    if (numLower == 0) or (numUpper == 0) or (numNumber == 0):
        return False
    return True


acc = input("Account : ")
pas = input("Password: ")

if (checkPassword(pas) == True):
    print("Notice: OK")
else:
    print("Notice: Fail")
