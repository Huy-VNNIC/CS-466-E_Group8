#Input: Danh sách lst chứa các số nguyên.
#Output: Trung bình cộng của tất cả phần tử và trung bình cộng của các phần tử dương.

#Các bước thuật toán:

#Tính tổng và độ dài của lst để tìm trung bình cộng của cả danh sách.
#Lọc các phần tử dương, tính tổng và số lượng của chúng để tìm trung bình cộng của các phần tử dương.

lst = [12, -14, 11, 91, -3, 10, 7, 15]

# Khởi tạo các biến để đếm và tính tổng các số dương
count_positive = 0
sum_positive = 0

# Tính tổng và đếm số lượng các phần tử dương trong danh sách
for num in lst:
    if num > 0:
        count_positive += 1    # Tăng biến đếm khi gặp một số dương.
        sum_positive += num     # Cộng số dương vào tổng số dương.

# Tính trung bình cộng của cả danh sách
average_all = sum(lst) / len(lst)

# Tính trung bình cộng các phần tử dương, kiểm tra để tránh chia cho 0
average_positive = sum_positive / count_positive if count_positive > 0 else 0  # Tránh chia cho 0

# Hiển thị kết quả
print("Trung bình cộng của cả danh sách:", average_all)
print("Trung bình cộng các phần tử dương:", average_positive)
