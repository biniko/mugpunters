from datetime import date

from django.db import models


# Create your models here.
# from accounts.models import CustomUser


class Season(models.Model):
    year = models.IntegerField()

    def __str__(self):
        return str(self.year)


class Team(models.Model):
    name = models.CharField(max_length=50)
    logo_url = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Round(models.Model):
    objects = models.Manager()
    number = models.IntegerField()
    date = models.DateField()
    start_time = models.TimeField()

    def __str__(self):
        return f"{self.number}"


class Match(models.Model):
    objects = models.Manager()
    round = models.ForeignKey(Round, on_delete=models.CASCADE)
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_team')
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_team')

    def __str__(self):
        return f"Round {self.round} - {self.home_team} vs {self.away_team}"


class Tip(models.Model):
    # user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='tip_team')
    round = models.ForeignKey(Round, on_delete=models.CASCADE, related_name='tip_round')
    submitted_date_time = models.DateField()

    def __str__(self):
        return f"Round {self.round} {self.team}"
