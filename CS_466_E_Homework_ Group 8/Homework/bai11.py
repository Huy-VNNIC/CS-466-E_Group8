#Input: Một danh sách các số nguyên: a = [2, -3, 4, -5, -1, 6, -7, 8, -9].
#Output: Độ dài của chuỗi các phần tử liên tiếp đan dấu nhiều nhất.

def max_alternating_sign_length(a):
    max_length = 0  # Biến để lưu độ dài chuỗi đan dấu dài nhất
    current_length = 1  # Biến để đếm chuỗi đan dấu hiện tại (bắt đầu với 1)

    for i in range(1, len(a)):
        # Kiểm tra hai phần tử liên tiếp đan dấu (tích của chúng âm)
        if a[i] * a[i - 1] < 0:
            current_length += 1  # Tăng độ dài chuỗi đan dấu hiện tại
        else:
            # Cập nhật max_length nếu current_length lớn hơn
            max_length = max(max_length, current_length)
            current_length = 1  # Đặt lại current_length

    # Cập nhật lại max_length lần cuối sau vòng lặp
    max_length = max(max_length, current_length)

    return max_length


a = [2, -3, 4, -5, -1, 6, -7, 8, -9]
print("Độ dài chuỗi đan dấu dài nhất =", max_alternating_sign_length(a))
