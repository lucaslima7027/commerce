from django.contrib import admin
from .models import *

# Register your models here.

class AuctionListingAdmin(admin.ModelAdmin):
    list_display = ("title", "category")

admin.site.register(User)
admin.site.register(AuctionListing, AuctionListingAdmin)
admin.site.register(Bid)
admin.site.register(Comment)
admin.site.register(UsersWatchList)
