from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from .models import Sport, League, Team, Match, Position
from accounts.models import CustomUser 
from django.contrib.auth.decorators import login_required
from accounts.forms import MatchForm, CoachForm, PlayerForm
import logging
from django.contrib.auth import login
from accounts.forms import CustomUserCreationForm

# Set up logging
logger = logging.getLogger(__name__)

class HomePageView(TemplateView):
    template_name = 'app/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sports'] = Sport.objects.all()
        return context

class AboutPageView(TemplateView):
    template_name = 'app/about.html'

class ContactPageView(TemplateView):
    template_name = 'app/contact.html'

class DashboardPageView(TemplateView):
    template_name = 'app/dashboard.html'

class MatchesListView(ListView):
    template_name = 'app/matches/matches_list.html'
    model = Match
    context_object_name = 'matches'


def match_list(request):
    matches = Match.objects.all()  # Query to get all matches
    return render(request, 'matches_list.html', {'matches': matches})



class MatchesDetailView(DetailView):
    template_name = 'app/matches/matches_detail.html'
    model = Match
    context_object_name = 'match'
    

class MatchesCreateView(CreateView):
    template_name = 'app/matches/matches_create.html'
    model = Match
    fields = ['league', 'team1', 'team2', 'sport', 'date', 'location']
    success_url = reverse_lazy('dashboard')

class MatchesUpdateView(UpdateView):
    template_name = 'app/matches/matches_update.html'
    model = Match
    fields = ['league', 'team1', 'team2', 'sport', 'date', 'location']
    success_url = reverse_lazy('dashboard')

class MatchesDeleteView(DeleteView):
    template_name = 'app/matches/matches_delete.html'
    model = Match
    success_url = reverse_lazy('dashboard')

class SportsListView(ListView):
    template_name = 'app/sports/sports_list.html'
    model = Sport
    context_object_name = 'sports'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query =self.request.GET.get('q', '')
        if query:
            filtered_sports = Sport.objects.filter(sport_name__icontains=query)
        else:
            filtered_sports = Sport.objects.all()
            context['sports'] = filtered_sports
        context['total_sports'] = Sport.objects.count()
        return context
        

class SportsDetailView(DetailView):
    template_name = 'app/sports/sports_detail.html'
    model = Sport
    context_object_name ='sport'

class SportsCreateView(CreateView):
    template_name = 'app/sports/sports_create.html'
    model = Sport
    fields = ['sport_name', 'description', 'rules', 'history']

class SportsUpdateView(UpdateView):
    template_name = 'app/sports/sports_update.html'
    model = Sport
    fields = ['sport_name', 'description', 'rules', 'history']
    success_url = reverse_lazy('dashboard')

class SportsDeleteView(DeleteView):
    template_name = 'app/sports/sports_delete.html'
    model = Sport
    success_url = reverse_lazy('dashboard')

class LeaguesListView(ListView):
    template_name = 'app/leagues/leagues_list.html'
    model = League
    context_object_name = 'leagues'

class LeaguesDetailView(DetailView):
    template_name = 'app/leagues/leagues_detail.html'
    model = League
    context_object_name = 'league'

class LeaguesCreateView(CreateView):
    template_name = 'app/leagues/leagues_create.html'
    model = League
    fields = ['league_name', 'sport', 'location', 'start_date', 'end_date']

class LeaguesUpdateView(UpdateView):
    template_name = 'app/leagues/leagues_update.html'
    model = League
    fields = ['league_name', 'sport', 'location', 'start_date', 'end_date']

class LeaguesDeleteView(DeleteView):
    template_name = 'app/leagues/leagues_delete.html'
    model = League
    success_url = reverse_lazy('leagues')

class TeamsListView(ListView):
    template_name = 'app/teams/teams_list.html'
    model = Team
    context_object_name = 'teams'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_teams'] = Team.objects.count()
        return context
    

class TeamsDetailView(DetailView):
    template_name = 'app/teams/teams_detail.html'
    model = Team
    context_object_name = 'team'

class TeamsCreateView(CreateView):
    template_name = 'app/teams/teams_create.html'
    model = Team
    fields = ['team_name', 'coach', 'sport', 'league']
    success_url = reverse_lazy('dashboard')

class TeamsUpdateView(UpdateView):
    template_name = 'app/teams/teams_update.html'
    model = Team
    fields = ['team_name', 'coach', 'sport', 'league']
    success_url = reverse_lazy('dashboard')

class TeamsDeleteView(DeleteView):
    template_name = 'app/teams/teams_delete.html'
    model = Team
    success_url = reverse_lazy('dashboard')

class PlayerDashboardView(TemplateView):
    template_name = 'app/dashboard/player_dashboard.html'

class CoachDashboardView(TemplateView):
    template_name = 'app/dashboard/coach_dashboard.html'

class AdminDashboardView(TemplateView):
    template_name = 'app/dashboard/admin_dashboard.html'

class UsersListView(ListView):
    template_name = 'app/users/users_list.html'
    model = CustomUser
    context_object_name = 'users'  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_users'] = CustomUser.objects.count()
        return context
    class UsersListView(ListView):
        template_name = 'app/users/users_list.html'
    model = CustomUser
    context_object_name = 'users'  # All users initially
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Separate users by their role (e.g., 'player', 'coach')
        players = CustomUser.objects.filter(role='player')  # Assuming role is a field in CustomUser model
        coaches = CustomUser.objects.filter(role='coach')  # Filter users by coach role
        
        context['total_users'] = CustomUser.objects.count()
        context['total_players'] = players.count()
        context['total_coaches'] = coaches.count()
        context['players'] = players
        context['coaches'] = coaches
        
        return context


class UsersDetailView(DetailView):
    template_name = 'app/users/users_detail.html'
    model = CustomUser
    context_object_name = 'user'

class UsersCreateView(CreateView):
    template_name = 'app/users/users_create.html'
    model = CustomUser
    fields = ['first_name', 'last_name', 'age']
    success_url = reverse_lazy('dashboard')

class UsersUpdateView(UpdateView):
    template_name = 'app/users/users_update.html'
    model = CustomUser
    fields = ['first_name', 'last_name', 'age']
    success_url = reverse_lazy('dashboard')

class UsersDeleteView(DeleteView):
    template_name = 'app/users/users_delete.html'
    model = CustomUser
    success_url = reverse_lazy('dashboard')

class PositionListView(ListView):
    template_name = 'app/position/position_list.html'
    model = Position
    context_object_name = 'positions'

class PositionDetailView(DetailView):
    template_name = 'app/position/position_detail.html'
    model = Position
    context_object_name ='position'

class PositionCreateView(CreateView):
    template_name = 'app/position/position_create.html'  # Updated to the correct template
    model = Position
    fields = ['sport', 'position_name']
    success_url = reverse_lazy('dashboard')

class PositionUpdateView(UpdateView):
    template_name = 'app/position/position_update.html'
    model = Position
    fields = ['sport', 'position_name']
    success_url = reverse_lazy('dashboard')

class PositionDeleteView(DeleteView):
    template_name = 'app/position/position_delete.html'
    model = Position
    success_url = reverse_lazy('dashboard')


def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

def coach_dashboard(request):
    return render(request, 'coach_dashboard.html')

def player_dashboard(request):
    return render(request, 'player_dashboard.html')

@login_required
def dashboard(request):
    return render(request, 'app/dashboard.html', {'user': request.user})


def create_match(request):
    leagues = League.objects.all()
    teams = Team.objects.all()
    sports = Sport.objects.all()

    if request.method == "POST":
        form = MatchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('matches_list')  # Redirect to match list page
    else:
        form = MatchForm()

    return render(request, 'app/match_form.html', {
        'form': form,
        'leagues': leagues,
        'teams': teams,
        'sports': sports,
    })

def signup(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        if user_form.is_valid():
            # Create the user
            user = user_form.save()

            # Create Player or Coach based on selected role
            role = user_form.cleaned_data['role']
            if role == 'player':
                player_form = PlayerForm(request.POST)
                if player_form.is_valid():
                    player = player_form.save(commit=False)
                    player.user = user  # Link the player to the created user
                    player.save()

            elif role == 'coach':
                coach_form = CoachForm(request.POST)
                if coach_form.is_valid():
                    coach = coach_form.save(commit=False)
                    coach.user = user  # Link the coach to the created user
                    coach.save()

            # Login the user after registration
            login(request, user)

            return redirect('home')  # Redirect to the home page after successful signup

    else:
        user_form = CustomUserCreationForm()

    return render(request, 'signup.html', {'user_form': user_form})
from django.shortcuts import render
from .models import Sport, Team, User, Match

def dashboard_view(request):
    # Fetch counts for each model
    sport_count = Sport.objects.count()
    team_count = Team.objects.count()
    user_count = User.objects.count()
    matches_count = Match.objects.count()

    context = {
        'sport': sport_count,
        'team': team_count,
        'total_users': user_count,
        'matches': matches_count,
    }

    return render(request, 'your_template.html', context)
