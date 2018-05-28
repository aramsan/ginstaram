from django.db import models


class Profile(models.Model):
    username = models.CharField(db_index=True, max_length=100)
    password = models.CharField(max_length=64)
    picture = models.CharField(max_length=64, default=None)

class Follow(models.Model):
    followee = models.ForeignKey('users.Profile', on_delete=models.SET_NULL, null=True, related_name="user_followed")
    follower = models.ForeignKey('users.Profile', on_delete=models.SET_NULL, null=True, related_name="user_foolowing")
