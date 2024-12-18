#Input: Danh sách lst chứa các số nguyên.
#Output: Số lượng các phần tử dương và tổng của các phần tử dương.

# Các bước thuật toán:

#Khởi tạo positive_count và positive_sum là 0.
#Duyệt qua từng phần tử trong danh sách:
#Nếu phần tử dương, tăng positive_count và cộng giá trị của phần tử vào positive_sum.
#Trả về positive_count và positive_sum.

lst = [12, -14, 11, 91, -3, 10, 7, 15]  # Danh sách cần được khai báo
count_positive = 0  # Biến đếm số lượng phần tử dương
sum_positive = 0    # Biến tổng các phần tử dương

for num in lst:  
    if num > 0:     # Kiểm tra nếu phần tử dương
        count_positive += 1     #Tăng biến đếm khi gặp một số dương.
        sum_positive += num # Cộng số dương vào tổng số dương.

print("Số lượng các phần tử dương:", count_positive) 
print("Tổng các phần tử dương:", sum_positive)
