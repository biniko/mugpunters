from datetime import date

from django.db import models

from django.core.exceptions import ValidationError


# Create your models here.
# from accounts.models import CustomUser


class Season(models.Model):
    year = models.IntegerField()

    def __str__(self):
        return str(self.year)


class Team(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    logo_url = models.CharField(max_length=50, null=True, blank=True)

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
    class Meta:
        verbose_name_plural = "Matches"

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

    def clean(self):
        if not self.pk:
            # No PK, means we are in add mode
            # We are in add mode, so we need to check if this round has already been submitted
            existing = Tip.objects.filter(round=self.round)
            if existing:
                raise ValidationError({'round': "A tip for this round has already been submitted."})

        # Now we check if this tip has the same team selected as the last round.
        # We do this in add or edit mode.
        existing = Tip.objects.filter(round=self.round.number - 1, team=self.team)
        if existing:
            raise ValidationError("The same team cannot be picked in two consecutive rounds. Please pick a different "
                                  "team.")

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
