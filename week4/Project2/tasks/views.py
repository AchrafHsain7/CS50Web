from django.shortcuts import render

TASKS = ["foo", "bar", "baz", "bor"]
# Create your views here.
def index(request):
    return render(request, 'tasks/index.html', {
        "tasks" : TASKS
    }) 

def add(request):
    return render(request, 'tasks/add.html')
