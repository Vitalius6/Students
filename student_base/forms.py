from django.forms import ModelForm
from student_base.models import Group, Student


class GroupForm(ModelForm):

    class Meta:
        model = Group
        fields = ['name', 'starosta']


class StudentForm(ModelForm):

    class Meta:
        model = Student
        fields = ['name', 'birth_day', 'ticket_number', 'group_names']