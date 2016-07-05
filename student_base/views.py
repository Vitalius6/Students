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

    def create_group(self, request):
        template_name = 'create_group.html'
        form = GroupForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('/')
        return render(request, template_name, {'form':form})


class EditGroup(generic.UpdateView):
    model = Group
    success_url = '/'
    fields = ['name', 'starosta']
    template_name = 'edit_group.html'

    def edit_group(self, request, pk):
        template_name = 'edit_group.html'
        pk = self.object.group_names.pk
        group = get_object_or_404(Group, pk=pk)
        form = GroupForm(request.POST or None, instance=group)
        if form.is_valid():
            form.save()
            return redirect('/')
        return render(request, template_name, {'form':form})


class DeleteGroup(generic.DeleteView):
    model = Group
    success_url = '/'
    template_name = 'delete_group.html'

    def delete_group(self, pk):
        group = get_object_or_404(Group, pk=pk)
        group.delete()
        return redirect('/')

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










