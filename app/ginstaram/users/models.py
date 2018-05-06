from django.db import models


class Profile(models.Model):
    username = models.CharField(db_index=True, max_length=100)
    password = models.CharField(max_length=64)

