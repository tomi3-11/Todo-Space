from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm, EditForm
from django.contrib import messages

# Create your views here.

def display_task(request):
    #title = get_object_or_404(Task, id=task_id)
    tasks = Task.objects.all()

    status_filter = request.GET.get('status')
    if status_filter in ['pending', 'completed', 'cancelled', 'incomplete']:
        tasks = tasks.filter(status=status_filter)

    context = {'tasks': tasks}
    return render(request, 'todoapp/display_task.html', context)


def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid:
            form.save()

            return redirect('todoapp:display_task')
    else:
        form = TaskForm()

    context = {'form': form }
    return render(request, 'todoapp/create_task.html', context)


def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        form = EditForm(request.POST, instance=task)
        if form.is_valid:
            form.save()

            # messages.success(request, "Task Updated successfully")
            return redirect('todoapp:display_task')
    else:
        form = EditForm(instance=task)

    context = {'form': form, 'task': task}
    return render(request, 'todoapp/edit_task.html', context)


def delete_task(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=task_id)
        task.delete()
        messages.success(request, "Task deleted successfully.")
        return redirect('todoapp:display_task')
    else:
        return render(request, 'todoapp/comfirm_delete_task.html')


def home(request):
    return render(request, 'todoapp/home.html')
