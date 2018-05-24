from django.db import models

class Post(models.Model):
    postid = models.AutoField(primary_key=True)
    author = models.ForeignKey('users.Profile', on_delete=models.SET_NULL, null=True)
    picture = models.CharField(max_length=64, default=None)
    text = models.TextField(blank=True)
    like = models.IntegerField(default = 0)
    time = models.DateTimeField(auto_now=True)

