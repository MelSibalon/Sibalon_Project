from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings
from accounts.models import CustomUser

SPORT_ICONS = {
    "Football": "icons/football.png",
    "Basketball": "icons/basketball.png",
    "Tennis": "icons/tennis.png",
    "Baseball": "icons/baseball.png",
}

class Sport(models.Model):
    sport_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    rules = models.TextField(blank=True, null=True)
    history = models.TextField(blank=True, null=True)
    icon_path = models.CharField(max_length=255, blank=True)  # Local file path

    def save(self, *args, **kwargs):
        # Automatically assign the local icon path based on sport name
        if not self.icon_path and self.sport_name in SPORT_ICONS:
            self.icon_path = SPORT_ICONS[self.sport_name]
        super().save(*args, **kwargs)
    
    def __str__(self):  
        return self.sport_name
    
    def get_absolute_url(self):
        return reverse("sports_detail", kwargs={"pk": self.pk})


class Position(models.Model):
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE, related_name="positions")
    position_name = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.position_name} in {self.sport.sport_name}"
    
class League(models.Model):
    league_name = models.CharField(max_length=100)
    sport = models.ManyToManyField(Sport, related_name="leagues")
    location = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.league_name
    
    def get_absolute_url(self):
        return reverse("leagues_detail", kwargs={"pk": self.pk})

class Team(models.Model):
    team_name = models.CharField(max_length=100)
    coach = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name="coached_teams")
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE, related_name="teams")
    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name="teams")

    def __str__(self):
        return self.team_name
    
    def get_absolute_url(self):
        return reverse('teams_detail', kwargs={'pk': self.pk})
    

class Match(models.Model):
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    team1 = models.ForeignKey(Team, related_name='team1_matches', on_delete=models.CASCADE)
    team2 = models.ForeignKey(Team, related_name='team2_matches', on_delete=models.CASCADE)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    date = models.DateTimeField()
    location = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.team1} vs {self.team2} - {self.date.strftime('%Y-%m-%d')}"
    
    class Meta:
        verbose_name_plural = "Matches"

class Registration(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="registrations")
    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name="registrations")
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE, related_name="registrations")
    registration_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} registered for {self.league.league_name}"
