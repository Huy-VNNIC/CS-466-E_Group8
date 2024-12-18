DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # PostgreSQL: django.db.backends.postgresql
        'NAME': BASE_DIR / 'db.sqlite3',         # Đường dẫn hoặc tên DB
    }
}

# myapp/views.py

from django.shortcuts import render
from .models import Student

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def add_student(request):
    student = Student(name='Huy', age=20, email='huy@gmail.com')
    student.save()
    return render(request, 'add_student.html', {'student': student})
