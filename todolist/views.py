from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404

# Create your views here.

from .models import Task


def tasks_view(request):
    tasks = Task.objects.all()

    return render(request, 'index.html', {'tasks': tasks})


def create_task_view(request):
    task = Task.objects.create(name=request.POST.get('task_name'))
    return redirect('tasks_view')


def edit_task_view(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'GET':
        return render(request, 'edit_task.html', {'task': task})
    elif request.method == 'POST':
        task.name = request.POST.get('task_name')
        task.description = request.POST.get('task_description')
        task.status = request.POST.get('task_status')
        task.save()
        return redirect('tasks_view')


def delete_task_view(request, task_id=None):
    if task_id:
        task = get_object_or_404(Task, pk=task_id)
    else:
        tasks = Task.objects.filter(status='done')
        if not tasks:
            return redirect('tasks_view')
    if request.method == 'GET' and task_id:
        return render(request, 'delete_task.html', {'task': task})
    elif request.method == 'GET' and not task_id:
        return render(request, 'delete_done_tasks.html')
    elif request.method == 'POST':
        if request.POST.get('delete') == 'yes':
            if task_id:
                task.delete()
            else:
                for task in tasks:
                    task.delete()
        return redirect('tasks_view')
