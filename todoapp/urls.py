# Defining the URLS for the todoapp 

from django.urls import path
from todoapp import views

app_name = 'todoapp'
urlpatterns = [
    path('', views.home, name='home'),
    path('tasks/', views.display_task, name='display_task'),
    path('tasks/create_task/', views.create_task, name='create_task'),
    path('task/edit_task/<int:task_id>/', views.edit_task, name='edit_task'),
    path('tasks/delete_task/<int:task_id>/', views.delete_task, name='confirm_delete_task')
]