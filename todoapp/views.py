from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm, EditForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from .utils import TaskCalendar
from datetime import datetime

# Create your views here.

def display_task(request):
    tasks = Task.objects.all()
    status_filter = request.GET.get('status')

    if status_filter in ['pending', 'completed', 'cancelled', 'incomplete']:
        tasks = tasks.filter(status=status_filter)

    context = {
        'tasks': tasks,
        'status_filter': status_filter  # pass it to the template
    }
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

            messages.success(request, "Task Updated successfully")
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


# Calendar View
def calendar_view(request):
    # Get month and year from the URL or use current
    month = int(request.GET.get('month', datetime.now().month))
    year = int(request.GET.get('year', datetime.now().year))
    
    if month < 1:
        month = 12
        year -= 1
    elif month > 12:
        month = 1
        year += 1
    
    tasks = Task.objects.all()
    cal = TaskCalendar(tasks).formatmonth(year, month)
    context = {
        'calendar': cal,
        'month': month,
        'year': year,
    }
    
    return render(request, 'todoapp/calendar.html', context)
