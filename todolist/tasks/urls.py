
from django.urls import path
from .views import task_list, add_task, update_task, mark_completed, delete_task

urlpatterns = [
    path('', task_list, name='task_list'),
    path('add/', add_task, name='add_task'),
    path('update/<int:task_id>/', update_task, name='update_task'),
    path('mark_completed/<int:task_id>/', mark_completed, name='mark_completed'),
    path('delete/<int:task_id>/', delete_task, name='delete_task'),
]
