# Input: lst = [12, -14, 11, 91, -3, 10, 7, 15]
# Output: Số lượng các số dương liên tiếp có tổng lớn nhất.

# Thuật toán:

# B1. Khởi tạo các biến tong_lon_nhat, so_luong_lon_nhat, tong_hien_tai, và so_luong_hien_tai bằng 0.
# B2. Duyệt qua từng phần tử trong danh sách:
#    - Nếu gặp số dương, tăng so_luong_hien_tai và cộng giá trị vào tong_hien_tai.
#    - Nếu gặp số không dương, so sánh tong_hien_tai với tong_lon_nhat:
#      - Nếu tong_hien_tai lớn hơn tong_lon_nhat, cập nhật tong_lon_nhat và so_luong_lon_nhat.
#      - Đặt lại tong_hien_tai và so_luong_hien_tai về 0 để bắt đầu chuỗi dương mới (nếu có).
# B3. Sau khi vòng lặp kết thúc, kiểm tra lần cuối xem tong_hien_tai có lớn hơn tong_lon_nhat hay không.
# B4. In kết quả là so_luong_lon_nhat - số lượng các số dương liên tiếp có tổng lớn nhất.

# Danh sách đầu vào
lst = [12, -14, 11, 91, -3, 10, 7, 15]

# Khởi tạo các biến
tong_lon_nhat = 0         # Tổng lớn nhất của các số dương liên tiếp
so_luong_lon_nhat = 0      # Số lượng các số dương liên tiếp có tổng lớn nhất
tong_hien_tai = 0          # Tổng hiện tại của các số dương liên tiếp
so_luong_hien_tai = 0      # Số lượng các số dương liên tiếp hiện tại

# Duyệt qua danh sách
for so in lst:
    if so > 0:
        tong_hien_tai += so           # Cộng số dương vào tổng hiện tại
        so_luong_hien_tai += 1        # Tăng biến đếm khi gặp một số dương
    else:
        # Nếu gặp số không dương, kiểm tra và cập nhật tổng lớn nhất và số lượng lớn nhất nếu cần
        if tong_hien_tai > tong_lon_nhat:
            tong_lon_nhat = tong_hien_tai
            so_luong_lon_nhat = so_luong_hien_tai
        # Đặt lại tổng hiện tại và số lượng hiện tại cho chuỗi dương tiếp theo
        tong_hien_tai = 0
        so_luong_hien_tai = 0

# Kiểm tra lại lần cuối sau khi kết thúc vòng lặp
if tong_hien_tai > tong_lon_nhat:
    tong_lon_nhat = tong_hien_tai
    so_luong_lon_nhat = so_luong_hien_tai

# In kết quả
print("Số lượng các số dương liên tiếp có tổng lớn nhất:", so_luong_lon_nhat)