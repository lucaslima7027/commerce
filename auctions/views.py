from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import *


def index(request):
    return render(request, "auctions/index.html",{
        "active_listings": Bid.objects.all()
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

def new_listing(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        starting_bid = request.POST["starting_bid"]
        img_url = request.POST["img_url"]
        category = request.POST["category"]

        listing = Auction_listing(title=title,
                                  description=description,
                                  starting_bid=starting_bid,
                                  img_url=img_url,
                                  category=category)
        listing.save()
        starting_bid = Bid(item=listing, bid_value=listing.starting_bid)
        starting_bid.save()
        return HttpResponseRedirect(reverse("index"))

    return render(request, "auctions/new_listing.html")

def detail(request, item_title):
    detailed_item = Bid.objects.get(item__title = item_title)
    if request.method == "POST":
        actual_bid = detailed_item.bid_value
        bid_recived = float(request.POST["bid"])

        if bid_recived > actual_bid:
            detailed_item.bid_value=bid_recived
            detailed_item.save()
            return render(request, "auctions/detail.html",{
        "detailed_item": detailed_item
        })
        
        else:
            message = "Your bid must be greater than current bid"
            return render(request, "auctions/detail.html",{
        "detailed_item": detailed_item,
        "message": message
    })
    
    return render(request, "auctions/detail.html",{
        "detailed_item": detailed_item
    })

def watch_list(request):
    username = request.user.username
    current_user = User.objects.get(username=username)
    watch_list = current_user.watch_list.all()

    return render(request, "auctions/watch_list.html", {
        "watch_list": watch_list
    })

    

