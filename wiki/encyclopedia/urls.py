from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("newpage", views.new_page, name="new_page"),
    path("editpage", views.edit_page, name="edit_page"),
    path("edited", views.edited, name="edited"),
    path("<str:entry>", views.display_entry, name="display_entry")
    
]

