from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from models import Group, Student


class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'starosta']

def create_group(request):
    template_name = 'create_group.html'
    form = GroupForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, template_name, {'form':form})

def server_update(request, pk):
    template_name = 'edit_group.html'
    group = get_object_or_404(Group, pk=pk)
    form = GroupForm(request.POST or None, instance=group)
    if form.is_valid():
        form.save()
        return redirect('server_list')
    return render(request, template_name, {'form':form})

def server_delete(request, pk):
    template_name = 'delete_group.html'
    group = get_object_or_404(Group, pk=pk)
    if request.method=='POST':
        group.delete()
        return redirect('server_list')
    return render(request, template_name, {'object':group})