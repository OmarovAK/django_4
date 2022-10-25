from django.contrib import admin
from .models import Teacher, Student, Student_teacher


class Student_inlines(admin.TabularInline):
    model = Student_teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', ]
    list_filter = ['subject']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'group', ]
    list_filter = ['group', ]
    inlines = [Student_inlines, ]
