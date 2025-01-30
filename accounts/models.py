# accounts/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('player', 'Player'),
        ('coach', 'Coach'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    age = models.IntegerField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)

    # Common fields for both players and coaches
    sport = models.ForeignKey('app.Sport', on_delete=models.CASCADE, null=True, blank=True)
    team = models.ForeignKey('app.Team', on_delete=models.CASCADE, null=True, blank=True)
    league = models.ForeignKey('app.League', on_delete=models.CASCADE, null=True, blank=True)

    # Player-specific fields
    position = models.ForeignKey('app.Position', on_delete=models.CASCADE, null=True, blank=True)
    jersey_number = models.IntegerField(null=True, blank=True)

    # Coach-specific fields
    coaching_experience = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.username
