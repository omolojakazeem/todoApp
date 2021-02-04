from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *

def index(request):
    template = 'tasks/list.html'
    taskList = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
        return redirect('/')
    context= {
        'tasks':taskList,
        'taskForm':form,
    }
    return render(request,template,context)


def update_task(request,pk):
    template = 'tasks/update.html'
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST,instance=task)

        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'taskForm':form,
    }
    return render(request, template_name=template, context=context)


def delete_task(request,pk):
    template = 'tasks/delete.html'

    task = Task.objects.get(id=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('/')
        
    context = {
        'task':task,
    }
    return render(request, template_name=template,context=context)