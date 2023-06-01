from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
     pass


class Comment(models.Model):
    text = models.CharField(max_length=500, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comments")    
    date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"Comment of {self.user}" 


