s = "Nguyen Duc Hung"
'''
======== Basic method ======

s.capitalize()     # In hoa chữ cái đầu tiên của các từ trong chuỗi
s.upper()          # In hoa toàn bộ chuỗi
s.lower()          # In thường toàn bộ chuỗi
s.swapcase()       # Chuyển hoa thành thường, chuyển thường thành hoa
s.ljust(20,'*')    # Thêm vào sau mỗi chuỗi ký tự với tổng số phần tử bao gồm luôn chuỗi gốc
s.rjust(20,',')    # Thêm voà trước mỗi chuỗi ký tự với tổng số phần tử bao gồm luôn chuỗi gốc
s.center(20,'+')   # Thêm vào trước và sau mỗi chuỗi ký tự với tổng số phần tử bao gồm luôn chuỗi gốc
s.lstrip() hoặc s.lstrip('*')    # Huỷ bỏ khoảng trắng hoặc ký tự bên trái
s.rstrip() hoặc s.rstrip('*')    # Huỷ bỏ khoảng trắng hoặc ký tự bên phải
s.strip() hoặc s.strip('*')     # Huỷ bỏ khoảng trắng hoặc ký tự

s.find('string', start, end)    # Tìm kiếm từ trong chuỗi trong khoảng vị trí từ start -> end
'string' in s                   # Ktra từ có trong chuỗi hay không
s.index('string')               # Lấy ra vị trí của 1 từ đang tìm
s.replace(find,replace,index)   # Tìm và thay thế từ
s.isalnum()                     # Trả về True nếu chuỗi có ít nhất 1 ký tự và không có khoảng trắng, không có ký tự đặc biệt
s.isalpha()                     # Trả vể True nếu chuỗi không có khoảng trắng và ký tự đặc biệt
s.isdigit()                     # Trả về True nếu chuỗi là số
s.isspace()                     # Trả về True nếu chuỗi là khoảng trắng

'''

print(s.isalnum())
print(s.isalpha())
print(s.isdigit())
print(s.isspace())


'''
==== Split Strings: Cắt chuỗi ====
==== Join Strings: Nối chuỗi ====

s.split()       # Cắt chuỗi dựa vào khoảng trắng
s.split('*')    # Cắt chuỗi dựa vào ký tự
s.split(' ', 5) # Cắt chuỗi dựa vào ký tự và số lần cắt
k.join(list)    # Gộp list thành chuỗi, phân cách các từ trong chuỗi bằng 'k'

'''

s = "Nguyen Duc Hung Nguyen Duc Hung Nguyen Duc Hung"
# print(s.split('n', 3))

l = s.split()
print(l)

k = "***"
print(k.join(l))


'''
===== String Format Method =====
  ( xem trên: pyformat.info )
'''
