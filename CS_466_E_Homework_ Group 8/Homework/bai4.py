#Input: Danh sách lst chứa các số nguyên.
#Output: Vị trí của phần tử âm đầu tiên.

#Các bước thuật toán:

#Duyệt qua danh sách lst theo từng phần tử và vị trí.
#Khi gặp phần tử đầu tiên là số âm, trả về vị trí của nó.
lst = [12, -14, 11, 91, -3, 10, 7, 15]
position_negative = -1

for i, num in enumerate(lst):      #enumerate(lst): Hàm enumerate() trả về chỉ số và giá trị của từng phần tử trong danh sách.
    if num < 0:  # Kiểm tra nếu phần tử là âm
        position_negative = i  # Lưu vị trí của phần tử âm
        break

print("Vị trí của phần tử âm đầu tiên:", position_negative)
