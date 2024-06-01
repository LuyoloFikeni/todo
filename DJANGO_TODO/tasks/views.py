from django.shortcuts import render
from .models import Task
from .forms import TaskForm
from django.shortcuts import redirect

def index(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    context = {'tasks': tasks, 'form': form}
    return render(request, 'tasks/list.html', context)

def update(request, pk):
    task = Task.objects.get(pk=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect("/")
    context = {'form': form}
    return render(request, 'tasks/update.html', context)

def delete(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect("/")
    context = {'task': task}
    return render(request, 'tasks/delete.html', context)

