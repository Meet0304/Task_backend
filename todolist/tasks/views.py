# tasks/views.py
from django.shortcuts import render, redirect

tasks = []  # In-memory list to store tasks

def task_list(request):
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        tasks.append({'id': len(tasks) + 1, 'title': title, 'completed': False})
        return redirect('task_list')
    return render(request, 'tasks/add_task.html')

def update_task(request, task_id):
    task = next((t for t in tasks if t['id'] == int(task_id)), None)
    if task is not None:
        if request.method == 'POST':
            title = request.POST.get('title')
            task['title'] = title
            return redirect('task_list')
        return render(request, 'tasks/update_task.html', {'task': task})
    return redirect('task_list')

def mark_completed(request, task_id):
    task = next((t for t in tasks if t['id'] == int(task_id)), None)
    if task is not None:
        task['completed'] = not task['completed']
        return redirect('task_list')
    return redirect('task_list')

def delete_task(request, task_id):
    global tasks
    tasks = [t for t in tasks if t['id'] != int(task_id)]
    return redirect('task_list')
