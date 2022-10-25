from django.core.management.base import BaseCommand
import json
import os
from colledge.models import Teacher, Student, Student_teacher


class Command(BaseCommand):

    def handle(self, *args, **options):
        file = os.path.join(os.getcwd(), 'school.json')
        with open(file, encoding='utf-8') as f:
            data = json.load(f)
        list_from_json = list(data)
        list_id_teacher = list()
        list_id_student = list()
        for i in Teacher.objects.all():
            list_id_teacher.append(i.id)
        for i in Student.objects.all():
            list_id_student.append(i.id)
        print('Список id учителей с базы данных: ', list_id_teacher)
        print('Список id студентов с базы данных: ', list_id_student)
        for i in list_from_json:
            if i['model'] == 'school.teacher':
                if i['pk'] not in list_id_teacher:
                    Teacher.objects.create(id=i['pk'], name=i['fields']['name'], subject=i['fields']['subject'])
            if i['model'] == 'school.student':
                print(i)
                if i['pk'] not in list_id_student:
                    Student.objects.create(id=i['pk'], name=i['fields']['name'], group=i['fields']['group'])
                    Student_teacher.objects.create(student_id=i['pk'], teacher_id=i['fields']['teacher'])
