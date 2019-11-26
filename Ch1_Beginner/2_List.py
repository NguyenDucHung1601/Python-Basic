'''
l = [1,2,3,4,5]    # List

len(l)      # Chiều dài của list
l[i]        # Lấy ra phần tử trong list ở vị trí i
l = l + l   # Tăng gấp đôi danh sách list
l = l * 2   # Tăng gấp đôi danh sách list
l = l * 3   # Tăng gấp ba danh sách list
l[i] = value    # Cập nhật giá trị mới cho list
l[start:end]    # Lấy giá trị list từ vị trí start -> end


===== List Method =====

l.append(val)         # Thêm 1 phần tử vào cuối list
l.insert(index, val)  # Thêm phần từ vào vtri index+1
l.pop(index)          # Xoá phần tử ở vtri index
l.count(val)          # Đếm số lần xuất hiện của phần tử
l.sort()              # Sắp xếp list theo thứ tự tăng dần
l.reverse()           # Đảo ngược vtri phần tử
del l[index]          # Xoá phần tử tại vtri index
del l[from:to]        # Xoá phần tử từ vtri from -> to

'''

l = [1,2,3,4,5]

l = l + [5,6,7]   # thêm 1 hoặc nhiều phâng tử phần tử
l.append(9)       # thêm 1 phần tử
print(l)
print(l.count(5))

