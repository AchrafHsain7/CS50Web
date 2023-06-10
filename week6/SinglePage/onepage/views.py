from django.shortcuts import render
from django.http import HttpResponse, Http404

# Create your views here.
def index(request):
    return render(request, 'onepage/index.html')


text = ["Hi mom i am on the web", "Hello web for the 6845 time", "This is CS50W"]

def section(request, num):
    if 1<= num <= 3:
        return HttpResponse(text[num-1])
    return Http404("No such section");
