from django.shortcuts import render
from django.views import generic
from models import Group, Student
from django.contrib import auth

class ListGroups(generic.ListView):
    model = Group
    template_name = 'list_groups.html'
    context_object_name = 'groups'

    def get_context_data(self, **kwargs):
        context = super(ListGroups, self).get_context_data(**kwargs)
        return context


class DetailGroup(generic.DetailView):
    model = Student
    template_name = 'detail_group.html'
    context_object_name = 'student'

