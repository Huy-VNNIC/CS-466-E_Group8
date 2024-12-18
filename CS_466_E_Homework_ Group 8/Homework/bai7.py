#Input: lst = [12, -14, 11, 91, -3, 10, 7, 15]
#Output: Phần tử lớn thứ nhì và các vị trí của phần tử lớn thứ nhì trong danh sách.
#thuat toan:
#Sử dụng set() để tìm các giá trị duy nhất trong danh sách và sắp xếp để lấy giá trị lớn thứ nhì.
#Duyệt qua danh sách để tìm các vị trí của phần tử có giá trị bằng phần tử lớn thứ nhì.
#In kết quả.

lst = [12, -14, 11, 91, -3, 10, 7, 15]
unique_sorted_lst = sorted(set(lst), reverse=True)  # Sắp xếp danh sách theo thứ tự giảm dần, bỏ trùng
second_largest = unique_sorted_lst[1]  # Lấy phần tử lớn thứ nhì
second_largest_positions = [i for i, num in enumerate(lst) if num == second_largest]

print("Phần tử lớn thứ nhì:", second_largest)
print("Vị trí của các phần tử đạt giá trị lớn thứ nhì:", second_largest_positions)
