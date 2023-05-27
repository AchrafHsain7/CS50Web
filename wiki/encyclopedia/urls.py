from django.urls import path

from . import views


urlpatterns = [
    path("wiki/", views.index, name="index"),
    path("wiki/search", views.search, name="search"),
    path("wiki/newpage", views.new_page, name="new_page"),
    path("wiki/editpage", views.edit_page, name="edit_page"),
    path("wiki/edited", views.edited, name="edited"),
    path("wiki/randompage", views.random_page, name="random_page"),
    path("wiki/<str:entry>", views.display_entry, name="display_entry")
    
]

