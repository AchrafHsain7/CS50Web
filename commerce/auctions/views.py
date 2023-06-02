from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
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

class BiddingForm(forms.Form):
    bidding_price = forms.IntegerField(min_value=1)



def index(request):
    active_listings = Listing.objects.filter(active=True).all()
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


@login_required
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
                listing = Listing(creator=request.user, winning_user=request.user, starting_bid=starting_bid, current_price=starting_bid, title=title, description=description,
                                image=image_link, category=category, active=True)
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


def  listing(request, object_id):
    listed_object = Listing.objects.filter(id=object_id).first() 
    in_watchlist = None
    if listed_object is not None:
        if request.user.is_authenticated:
            if listed_object in request.user.user_watchlist.all():
                in_watchlist = True
            else:
                in_watchlist = False

        return render(request, 'auctions/listing.html', {
            "listing": listed_object,
            "in_watchlist": in_watchlist,
            "bidding_form": BiddingForm(), 
        }) 
    else:
        return HttpResponseRedirect(reverse("index"))
    


@login_required
def add_watchlist(request, object_id):
    listing = Listing.objects.filter(id=object_id).first()
    if listing is not None:
        request.user.user_watchlist.add(listing)
    return HttpResponseRedirect(reverse("listing_detail", args=(object_id,)))

@login_required
def remove_watchlist(request, object_id):
    listing = Listing.objects.filter(id=object_id).first()
    if listing is not None:
        request.user.user_watchlist.remove(listing) 
    return HttpResponseRedirect(reverse("listing_detail",args=(object_id,))) 

@login_required
def bidding_transaction(request, object_id):
    if request.method == "POST":
        listing = Listing.objects.filter(id=object_id).first()
        form = BiddingForm(request.POST)
        if listing is not None and form.is_valid():
            price = form.cleaned_data["bidding_price"]
            if price > int(listing.current_price):
                listing.current_price = price
                listing.winning_user = request.user
                listing.save(update_fields=['current_price', 'winning_user'])
                new_bid = Bid(user=request.user, listing=listing, amount=price)
                new_bid.save() 
            else:
                return HttpResponse("<h1>The transaction failed, Make sure the price is larger than the current price and object exist </h1>")
        return HttpResponseRedirect(reverse("listing_detail", args=(object_id,)))
    
    return HttpResponseRedirect("index") 

@login_required
def close_listing(request, object_id):
    listing = Listing.objects.filter(id=object_id).first()
    if listing is not None:
        listing.active = False
        listing.save(update_fields=["active"]) 
    return HttpResponseRedirect(reverse("listing_detail", args=(object_id,)))