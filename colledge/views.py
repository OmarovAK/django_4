from django.shortcuts import render
from .models import Student


def index_view(request):
    students = Student.objects.all()
    for d in students.all():
        for i in d.teacher.all():
            print(i)
    my_dict = {
        'title': 'Главная страница',
        'students': students,
    }
    return render(request, 'migrations/index.html', my_dict)
