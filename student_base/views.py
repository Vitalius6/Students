from django.views import generic
from models import Group, Student
from django.contrib import auth
from django.shortcuts import render, redirect, get_object_or_404
from student_base.forms import GroupForm, StudentForm

class ListGroups(generic.ListView):
    model = Group
    template_name = 'list_groups.html'
    context_object_name = 'groups'

    def get_context_data(self, **kwargs):
        context = super(ListGroups, self).get_context_data(**kwargs)
        return context


class DetailGroup(generic.DetailView):
    model = Group
    template_name = 'detail_group.html'


class CreateGroup(generic.CreateView):
    form_class = GroupForm
    success_url = '/'
    template_name = 'create_group.html'


class EditGroup(generic.UpdateView):
    model = Group
    success_url = '/'
    fields = ['name', 'starosta']
    template_name = 'edit_group.html'


class DeleteGroup(generic.DeleteView):
    model = Group
    success_url = '/'
    template_name = 'delete_group.html'


class CreateStudent(generic.CreateView):
    model = Student
    fields = ['name', 'birth_day', 'ticket_number', 'group_names']

    def get_success_url(self):
        pk = self.object.group_names.pk
        return '/{}/'.format(pk)


class EditStudent(generic.UpdateView):
    model = Student
    fields = ['name', 'birth_day', 'ticket_number', 'group_names']

    def get_success_url(self):
        pk = self.object.group_names.pk
        return '/{}/'.format(pk)


class DeleteStudent(generic.DeleteView):
    model = Student

    def get_success_url(self):
        pk = self.object.group_names.pk
        return '/{}/'.format(pk)










