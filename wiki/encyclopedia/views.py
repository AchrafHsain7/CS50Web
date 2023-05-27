from django.shortcuts import render
from . import util

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

