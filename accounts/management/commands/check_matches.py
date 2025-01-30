from django.core.management.base import BaseCommand
from app.models import Match

class Command(BaseCommand):
    help = 'Check existing matches in the database'

    def handle(self, *args, **kwargs):
        matches = Match.objects.all()
        if matches.exists():
            for match in matches:
                self.stdout.write(f'Match: {match.team1} vs {match.team2} on {match.date} at {match.location}')
        else:
            self.stdout.write(self.style.WARNING('No matches found in the database.'))
