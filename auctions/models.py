from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Auction_listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=64)
    starting_bid = models.FloatField()
    img_url = models.URLField()
    category = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.title} | {self.starting_bid} | {self.category}"

class Bid(models.Model):
    item = models.ForeignKey(Auction_listing, on_delete=models.CASCADE, related_name="item")
    bid_value = models.FloatField()

    def __str__(self):
        return f"{self.item.title} - {self.bid_value}"

class Comment(models.Model):
    pass
