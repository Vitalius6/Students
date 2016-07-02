from django.shortcuts import render
from django.views import generic
from models import Group, Student
from django.contrib import auth
from django.shortcuts import get_object_or_404

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
    model = Group
    success_url = '/'
    fields = ['name', 'starosta']


class EditGroup(generic.UpdateView):
    model = Group
    success_url = '/'
    fields = ['name', 'starosta']


class DeleteGroup(generic.DeleteView):
    model = Group
    success_url = '/'


class CreateStudent(generic.CreateView):
    model = Student
    success_url = '/'
    fields = ['name', 'birth_day', 'ticket_number', 'group_names']


class EditStudent(generic.UpdateView):
    model = Student
    success_url = '/'
    fields = ['name', 'birth_day', 'ticket_number', 'group_names']


class DeleteStudent(generic.DeleteView):
    model = Student
    success_url = '/'




