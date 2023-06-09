from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
     pass

class Listing(models.Model):
    creator = models.ForeignKey(User, blank=False, on_delete=models.CASCADE, related_name="user_listings") 
    winning_user = models.ForeignKey(User, blank=False, on_delete=models.CASCADE, related_name="user_winning_listings") 
    starting_bid = models.PositiveIntegerField(blank=False)
    current_price = models.PositiveIntegerField(blank=False)
    title = models.CharField(max_length=64, blank=False)
    description = models.CharField(max_length=500)
    image = models.URLField()
    category = models.CharField(max_length=50) 
    on_watchlist = models.ManyToManyField(User, blank=True, related_name="user_watchlist")
    active = models.BooleanField()

    def __str__(self):
        return f"{self.title}, Active: {self.active}"

class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_bids")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="listing_bids")
    amount = models.PositiveIntegerField(blank=False)
    date = models.DateTimeField(auto_now=True)  

    def __str__(self) -> str:
        return f"Created by {self.user} with amount {self.amount}"  


class Comment(models.Model):
    text = models.CharField(max_length=500, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comments")  
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="listing_comments", null=True) 
    date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"Comment of {self.user}" 



