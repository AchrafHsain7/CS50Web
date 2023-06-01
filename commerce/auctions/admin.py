from django.contrib import admin

from .models import *

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "user_comments", "user_listings", "user_bids"]    

    @admin.display(ordering="user__comment", description="User Comments")
    def user_comments(self, obj):
        return obj.user_comments.all() 
    @admin.display(ordering="user__listing", description="User Listings")
    def user_listings(self, obj):
        return obj.user_listings.all()
    @admin.display(ordering="user__bid", description="User Bids")
    def user_bids(self, obj):
        return obj.user_bids.all() 

class ListingAdmin(admin.ModelAdmin):
    list_display = ["creator", "title", "listing_bids"]   

    @admin.display(ordering="listing__bid", description="Bids")
    def listing_bids(self, obj):
        return obj.listing_bids.all() 
            

admin.site.register(User, UserAdmin)  
admin.site.register(Comment)   
admin.site.register(Listing, ListingAdmin)
admin.site.register(Bid) 





