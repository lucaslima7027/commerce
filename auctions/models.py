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

class Bids(models.Model):
    pass

class Comments(models.Model):
    pass
