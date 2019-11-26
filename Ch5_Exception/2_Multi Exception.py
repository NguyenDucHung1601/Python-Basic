'''

Multi exception: Xử lí nhiều lỗi
 các xử lỉ ngoại lệ phải đặt từ trên xuống dưới theo trình tự lỗi có thể xảy ra

'''

try:
    a = 1
    b = 0
    print("x = ", a / b)

    f = open("Hung.txt", "r")
    for line in f:
        print(line)
except ZeroDivisionError as error:
    print("Error: ", error)
except FileNotFoundError as error:
    print("Error: ", error)
