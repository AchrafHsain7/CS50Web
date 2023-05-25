from django.urls import path
from . import views

urlpatterns = [
    path('<str:name>', views.hello, name='hello'),
    path('', views.index, name='index')
]