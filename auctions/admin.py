from django.contrib import admin
from .models import *

# Register your models here.

class Auction_listingAdmin(admin.ModelAdmin):
    list_display = ("title", "category")

admin.site.register(User)
admin.site.register(Auction_listing, Auction_listingAdmin)
admin.site.register(Bids)
admin.site.register(Comments)
