from django.urls import path

from . import views

app_name = "wiki"
urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("newpage", views.new_page, name="new_page"),
    path("editpage/<str:title>", views.edit_page, name="editpage"),
    path("<str:entry>", views.display_entry, name="display_entry")
    
]

