from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class AuctionListing(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=64)
    starting_bid = models.FloatField()
    img_url = models.URLField()
    category = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.title} | {self.starting_bid} | {self.category}"


class Bid(models.Model):
    item = models.ForeignKey(AuctionListing, on_delete=models.CASCADE, related_name="item")
    bid_value = models.FloatField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, related_name="creator_info")
    open = models.BooleanField()
    winner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, related_name="winner_name")

    def __str__(self):
        return f"{self.item.title} - {self.bid_value}"


class UsersWatchList(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usernameWL")
    watch_list = models.ManyToManyField(Bid, blank=True, related_name="itens")

    def __str__(self):
        return f"{self.username} - {self.watch_list}"


class Comment(models.Model):
    person = models.ForeignKey("User", on_delete=models.CASCADE, blank=True)
    item = models.ForeignKey("AuctionListing", on_delete=models.CASCADE, blank=True)
    comment = models.TextField(max_length=64, blank=True)


