from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("createlisting", views.create_listing, name="create_listing"),
    path("listing/<str:object_id>", views.listing, name="listing_detail"), 
    path("add_watchlist/<str:object_id>", views.add_watchlist, name="add_watchlist"),
    path("remove_watchlist/<str:object_id>", views.remove_watchlist, name="remove_watchlist"),
    path("bid/<str:object_id>", views.bidding_transaction, name="bid"),
    path("closelisting/<str:object_id>", views.close_listing, name="close_listing"), 
    path("add_comment/<str:object_id>", views.add_comment, name="add_comment"), 
    path("watchlist", views.watchlist, name="watchlist"),
    path("categories", views.categories, name="categories"),
    path("categoriyListings/<str:category>", views.category_listings, name="category_listings")
]
