from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request, name):
    return render(request, 'hello/hello.html', {
        "name": name.capitalize()
    })

def index(request):
    return HttpResponse("Hello, world!")
