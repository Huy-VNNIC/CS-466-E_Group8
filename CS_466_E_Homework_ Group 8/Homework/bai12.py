#Input: Một danh sách các số nguyên a = [5, 3, 3, 2, 4, 4, 3, 2, 1].
#Output: Độ dài của chuỗi các phần tử liên tiếp dài nhất mà dãy không tăng.

def max_non_increasing_length(a):
    max_length = 1  # Độ dài lớn nhất của chuỗi không tăng
    current_length = 1  # Độ dài của chuỗi không tăng hiện tại

    for i in range(1, len(a)):
        # Kiểm tra nếu phần tử hiện tại lớn hơn hoặc bằng phần tử kế tiếp
        if a[i - 1] >= a[i]:
            current_length += 1  # Tăng độ dài của chuỗi không tăng
        else:
            # Cập nhật max_length nếu cần và đặt lại current_length
            max_length = max(max_length, current_length)
            current_length = 1

    # Kiểm tra lần cuối cùng nếu chuỗi không tăng nằm ở cuối danh sách
    max_length = max(max_length, current_length)

    return max_length


a = [5, 3, 3, 2, 4, 4, 3, 2, 1]
print("Độ dài chuỗi không tăng dài nhất =", max_non_increasing_length(a))
