from django.shortcuts import render
from . import util
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

from . import util

class SearchForm(forms.Form):
    to_search = forms.CharField()


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
    form = request.POST
    results = []
    if form.is_valid():
        to_search = form.cleaned_data["to_search"]
        if to_search in entries:
            return HttpResponseRedirect(to_search)
        else:
            for entry in entries:
                if to_search in entry:
                    results.append(entry)
            return render(request, 'encyclopedia/search.html', {
                "results": results
            })
                    

