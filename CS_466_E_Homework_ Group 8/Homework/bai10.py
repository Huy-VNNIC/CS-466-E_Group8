#Input: Danh sách lst chứa các số nguyên.
#Output: Số lượng các phần tử liên tiếp đan dấu nhiều nhất.

#Các bước thuật toán:

#Khởi tạo max_alternating_count và current_alternating_count bằng 1.
#Duyệt qua từng cặp phần tử trong danh sách.
#Nếu tích hai phần tử liên tiếp âm (đan dấu), tăng current_alternating_count.
#Cập nhật max_alternating_count nếu cần thiết.
lst = [12, -14, 11, 91, -3, 10, 7, 15]
max_alternating_count = 1
current_alternating_count = 1

for i in range(1, len(lst)):
    if lst[i] * lst[i - 1] < 0:
        current_alternating_count += 1
        max_alternating_count = max(max_alternating_count, current_alternating_count)
    else:
        current_alternating_count = 1

print("Số lượng các phần tử liên tiếp đan dấu nhiều nhất:", max_alternating_count)
