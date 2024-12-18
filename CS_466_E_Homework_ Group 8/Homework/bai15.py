# Thao tác với cơ sở dữ liệu trong Django

# Thêm dữ liệu
post = Post(title="Django ORM", content="Tìm hiểu ORM trong Django", author="Nguyễn  Nhật Huy")
post.save()  # Lưu bài viết vào cơ sở dữ liệu

# Lấy dữ liệu
posts = Post.objects.all()  # Lấy tất cả bài viết từ cơ sở dữ liệu

# Cập nhật dữ liệu
post = Post.objects.get(id=1)  # Lấy bài viết có id=1
post.title = "Cập nhật tiêu đề"  # Thay đổi tiêu đề bài viết
post.save()  # Lưu thay đổi vào cơ sở dữ liệu

# Xóa dữ liệu
post = Post.objects.get(id=1)  # Lấy bài viết có id=1
post.delete()  # Xóa bài viết khỏi cơ sở dữ liệu
