from .forms import CustomUserCreationForm, PlayerForm, CoachForm
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.http import JsonResponse
from accounts.models import CustomUser
import logging

logger = logging.getLogger(__name__)

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = form.cleaned_data['role']
            user.save()

            # Handle role-specific forms
            if user.role == 'player':
                player_form = PlayerForm(request.POST, instance=user)
                if player_form.is_valid():
                    player_form.save()
            elif user.role == 'coach':
                coach_form = CoachForm(request.POST, instance=user)
                if coach_form.is_valid():
                    coach_form.save()

            logger.info(f"User {user.username} signed up successfully.")
            return redirect('login')  # Redirect to login page or another page
    else:
        form = CustomUserCreationForm()

    return render(request, 'accounts/signup.html', {'form': form})


def user_management(request):
    # Fetch all users
    users = CustomUser.objects.all()
    
    # Filter players and coaches based on role
    players = users.filter(role='player')
    coaches = users.filter(role='coach')
    
    # Calculate total users, players, and coaches
    total_users = users.count()
    total_players = players.count()
    total_coaches = coaches.count()
    
    # Pass the filtered data to the template
    return render(request, 'users_list.html', {  # Correct template name
        'users': users,
        'players': players,
        'coaches': coaches,
        'total_users': total_users,
        'total_players': total_players,
        'total_coaches': total_coaches,
    })