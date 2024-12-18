#Input: Danh sách lst chứa các số nguyên.
#Output: Vị trí của phần tử dương cuối cùng.

#Các bước thuật toán:

#Duyệt ngược qua danh sách lst.
#Khi gặp phần tử dương đầu tiên từ cuối, trả về vị trí của nó.

lst = [12, -14, 11, 91, -3, 10, 7, 15]
position_positive = -1

for i in range(len(lst) - 1, -1, -1):
    if lst[i] > 0:  # Kiểm tra nếu phần tử là dương
        position_positive = i
        break

print("Vị trí của phần tử dương cuối cùng:", position_positive)
