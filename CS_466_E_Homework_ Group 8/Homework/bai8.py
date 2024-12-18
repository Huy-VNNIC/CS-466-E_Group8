#Input: lst = [12, -14, 11, 91, -3, 10, 7, 15]
#Output: Số lượng các số dương liên tiếp nhiều nhất.

#Thuật toán:
#Khởi tạo max_count và current_count bằng 0.
#Duyệt qua danh sách lst. Nếu gặp số dương, tăng current_count. 
#Nếu không, cập nhật max_count và đặt lại current_count.
#Sau khi kết thúc vòng lặp, kiểm tra lại max_count lần cuối.
#In kết quả.

lst = [12, -14, 11, 91, -3, 10, 7, 15]
max_count = 0
current_count = 0

for num in lst:
    if num > 0:
        current_count += 1
        max_count = max(max_count, current_count)
    else:
        current_count = 0

print("Số lượng các số dương liên tiếp nhiều nhất:", max_count)
