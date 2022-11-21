# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

from tips.models import Team


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    fav_team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.CASCADE, related_name='favourite_team')

