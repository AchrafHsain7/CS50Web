from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms

from .models import *

CATEGORIES = [('sport', 'Sport'), ('music', 'Music'), ('electronics', 'Electronics'), ('fashion', 'Fashion'), ('games', 'Games'), ('home', 'Home')
              , ('toys', 'Toys'), ('books', 'Books')]

#forms defined here
class ListingForm(forms.Form):
    title = forms.CharField(max_length=64)
    starting_bid = forms.IntegerField(min_value=0)
    description = forms.CharField(max_length=500)
    image_link = forms.URLField()
    category = forms.CharField(widget=forms.Select(choices=[x for x in CATEGORIES]))



def index(request):
    active_listings = Listing.objects.all()
    return render(request, "auctions/index.html", {
        "listings": active_listings
    })



def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def create_listing(request):
    if request.method == "POST":
        form = ListingForm(request.POST)
        if form.is_valid():
            starting_bid = int(form.cleaned_data["starting_bid"]) 
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            image_link = form.cleaned_data["image_link"]
            category = form.cleaned_data["category"]
            if True in [category in a for a in CATEGORIES]:
                listing = Listing(creator=request.user, winning_user=request.user, starting_bid=starting_bid,current_price=starting_bid, title=title, description=description,
                                image=image_link, category=category)
                listing.save()

                return HttpResponseRedirect(reverse("index"))
            else:
                return HttpResponse("<h1>Please enter a valid Category!</h1>") 
        
        else:
            return render(request, 'auctions/create_listing', {
                "form": form
            })

    return render(request, "auctions/create_listing.html", {
        "form": ListingForm()
    })