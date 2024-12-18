#Input: lst = [12, -14, 11, 91, -3, 10, 7, 15]
#Output: Phần tử lớn nhất và vị trí của phần tử lớn nhất cuối cùng trong danh sách.


#Thuật toán:

#Sử dụng hàm max() để tìm giá trị lớn nhất trong danh sách.
#Duyệt qua danh sách từ cuối về đầu để tìm vị trí cuối cùng của giá trị lớn nhất.
#In kết quả.
lst = [12, -14, 11, 91, -3, 10, 7, 15]
max_value = max(lst)
last_max_index = len(lst) - 1 - lst[::-1].index(max_value)

print("Phần tử lớn nhất:", max_value)
print("Vị trí của phần tử lớn nhất cuối cùng:", last_max_index)
