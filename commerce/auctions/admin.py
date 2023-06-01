from django.contrib import admin

from .models import *

# Register your models here.
class CommentsAdmin(admin.ModelAdmin):
    list_display = ["id"]

admin.site.register(User) 
admin.site.register(Comment, CommentsAdmin)  





