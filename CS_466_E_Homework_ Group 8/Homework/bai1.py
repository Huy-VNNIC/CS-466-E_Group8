#Input: Danh sách lst chứa các số nguyên
#Output: Tổng các phần tử trong danh sách.


# Các bước thuật toán:

#Khởi tạo biến total_sum là 0.
#Duyệt qua từng phần tử trong danh sách và cộng dồn vào total_sum.
#Trả về total_sum.
lst = [12, -14, 11, 91, -3, 10, 7, 15]
total = sum(lst)  # Hàm sum() tính tổng các phần tử trong danh sách
print("Tổng các phần tử trong danh sách:", total)
