from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Sport(models.Model):
    sport_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    rules = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.sport_name
    
    def get_absolute_url(self):
        return reverse("ms_detail", kwargs={"pk": self.pk})


class Position(models.Model):
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE, related_name="positions")
    position_name = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.position_name} in {self.sport.sport_name}"


class League(models.Model):
    league_name = models.CharField(max_length=100)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE, related_name="leagues")
    location = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.league_name


class Team(models.Model):
    team_name = models.CharField(max_length=100)
    coach = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="coached_teams")
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE, related_name="teams")
    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name="teams")

    def __str__(self):
        return self.team_name
    
class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="player_profile")
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, related_name="players")
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE, related_name="players")
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True, related_name="players")
    jersey_number = models.IntegerField(default=0)


    def __str__(self):
        return self.user.first_name, self.user.last_name


class Match(models.Model):
    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name="matches")
    team1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="matches_as_team1")
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="matches_as_team2")
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE, related_name="matches")
    date = models.DateTimeField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.team1} vs {self.team2} - {self.date.strftime('%Y-%m-%d')}"
    class Meta:
            verbose_name_plural = "Matches"


class Registration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="registrations")
    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name="registrations")
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE, related_name="registrations")
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} registered for {self.league.league_name}"


class Role(models.Model):
    ROLE_CHOICES = [
        ('Player', 'Player'),
        ('Coach', 'Coach'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="role")
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}" 
    
class Coach(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="coach_profile")

    def __str__(self):
        return f"Coach {self.user.username}"
    class Meta:
            verbose_name_plural = "Coaches"
