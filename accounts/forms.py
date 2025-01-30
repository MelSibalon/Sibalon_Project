from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from app.models import Team, League, Position, Match, Sport

# Define choices for the role
ROLE_CHOICES = [
    ('player', 'Player'),
    ('coach', 'Coach'),
]

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    role = forms.ChoiceField(choices=ROLE_CHOICES, required=True, label="Register as")

    # Common fields
    sport = forms.ModelChoiceField(queryset=Sport.objects.all(), required=False)
    team = forms.ModelChoiceField(queryset=Team.objects.all(), required=False)
    league = forms.ModelChoiceField(queryset=League.objects.all(), required=False)

    # Player-specific fields
    position = forms.ModelChoiceField(queryset=Position.objects.all(), required=False)
    jersey_number = forms.IntegerField(required=False)

    # Coach-specific fields
    coaching_experience = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'role',
                  'sport', 'team', 'league', 'position', 'jersey_number', 'coaching_experience']

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'age', 'phone_number')  # Removed 'role' field

class PlayerForm(forms.ModelForm):
    sport = forms.ModelChoiceField(queryset=Sport.objects.all(), required=True)
    team = forms.ModelChoiceField(queryset=Team.objects.all(), required=True)
    league = forms.ModelChoiceField(queryset=League.objects.all(), required=True)
    position = forms.ModelChoiceField(queryset=Position.objects.all(), required=True)
    jersey_number = forms.IntegerField(required=True)

    class Meta:
        model = CustomUser
        fields = ['sport', 'team', 'league', 'position', 'jersey_number']

class CoachForm(forms.ModelForm):
    sport = forms.ModelChoiceField(queryset=Sport.objects.all(), required=True)
    team = forms.ModelChoiceField(queryset=Team.objects.all(), required=True)
    league = forms.ModelChoiceField(queryset=League.objects.all(), required=True)
    coaching_experience = forms.CharField(widget=forms.Textarea, required=True)

    class Meta:
        model = CustomUser
        fields = ['sport', 'team', 'league', 'coaching_experience']

class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['league', 'team1', 'team2', 'sport', 'date', 'location']

class LeagueForm(forms.ModelForm):
    class Meta:
        model = League
        fields = ['league_name', 'sport', 'location', 'start_date', 'end_date']
        widgets = {
            'sport': forms.CheckboxSelectMultiple,  # Use checkboxes for multiple sports
        }
