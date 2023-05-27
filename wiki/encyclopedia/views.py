from django.shortcuts import render
from . import util
from django import forms
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from . import util



def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def display_entry(request, entry):
    entry_title = str(entry)
    entry_data = util.get_entry(entry_title)
    if entry_data == None:
        return render(request, 'encyclopedia/failure.html', {
            "error_code" : "ERROR 101",
            "error_message": "The requested entry does not exist yet"
        })
    return render(request, 'encyclopedia/entry.html', {
        "title": entry_title.capitalize(),
        "data" : entry_data
    })

def search(request):
    entries = util.list_entries()
    to_search = request.POST["to_add"]
    results = []
    if to_search.upper() in [entry.upper() for entry in entries]:
        return HttpResponseRedirect(to_search)
    else:
        for entry in entries:
            if to_search.upper() in entry.upper():
                results.append(entry)
        return render(request, 'encyclopedia/search.html', {
            "results": results
        })
   
def new_page(request):
    if request.method == "POST":
        existing_entries = util.list_entries()
        if request.POST["title"].upper() in [entry.upper() for entry in existing_entries]:
            return render(request, 'encyclopedia/failure.html', {
                "error_code" : "ERROR 102",
                "error_message" : "This Page already Exist! Maybe you want to edit it instead?"
            })
        util.save_entry(request.POST["title"], request.POST["MD_data"])
        return HttpResponseRedirect(request.POST["title"])
    
    return render(request, 'encyclopedia/new_page.html')

def edit_page(request):
    return render(request, 'encyclopedia/edit_page.html', {
        "title": request.POST["title"],
        "entry_data": util.get_entry(request.POST["title"])
    })
                    

