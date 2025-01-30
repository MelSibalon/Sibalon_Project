from django.urls import path
from . import views

from .views import match_list
from .views import (
    HomePageView, AboutPageView, ContactPageView,
    MatchesListView, MatchesDetailView, MatchesCreateView, MatchesUpdateView, MatchesDeleteView,
    SportsCreateView, SportsDeleteView, SportsDetailView, SportsListView, SportsUpdateView,
    LeaguesCreateView, LeaguesDeleteView, LeaguesDetailView, LeaguesUpdateView, LeaguesListView,
    TeamsCreateView, TeamsDeleteView, TeamsDetailView, TeamsListView, TeamsUpdateView,

    DashboardPageView, PlayerDashboardView, CoachDashboardView, AdminDashboardView,
    UsersListView, UsersDetailView, UsersCreateView, UsersDeleteView, UsersUpdateView,PositionCreateView,
    PositionDeleteView, PositionDetailView, PositionUpdateView, PositionListView,
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    # Sports URLs
    path('sports/', SportsListView.as_view(), name='sports'),
    path('sports/<int:pk>/', SportsDetailView.as_view(), name='sports_detail'),
    path('sports/create/', SportsCreateView.as_view(), name='sports_create'),
    path('sports/<int:pk>/edit/', SportsUpdateView.as_view(), name='sports_update'),
    path('sports/<int:pk>/delete/', SportsDeleteView.as_view(), name='sports_delete'),

    # Leagues URLs
    path('leagues/', LeaguesListView.as_view(), name='leagues'),
    path('leagues/<int:pk>/', LeaguesDetailView.as_view(), name='leagues_detail'),
    path('leagues/create/', LeaguesCreateView.as_view(), name='leagues_create'),
    path('leagues/<int:pk>/edit/', LeaguesUpdateView.as_view(), name='leagues_update'),
    path('leagues/<int:pk>/delete/', LeaguesDeleteView.as_view(), name='leagues_delete'),


    # Teams URLs
    path('teams/', TeamsListView.as_view(), name='teams'),
    path('teams/<int:pk>/', TeamsDetailView.as_view(), name='teams_detail'),
    path('teams/create/', TeamsCreateView.as_view(), name='teams_create'),
    path('teams/<int:pk>/edit/', TeamsUpdateView.as_view(), name='teams_update'),
    path('teams/<int:pk>/delete/', TeamsDeleteView.as_view(), name='teams_delete'),

    # Matches URLs
    path('matches/', MatchesListView.as_view(), name='matches'),
    path('matches/<int:pk>/', MatchesDetailView.as_view(), name='matches_detail'),
    path('matches/create/', MatchesCreateView.as_view(), name='matches_create'),
    path('matches/<int:pk>/edit/', MatchesUpdateView.as_view(), name='matches_update'),
    path('matches/<int:pk>/delete/', MatchesDeleteView.as_view(), name='matches_delete'),

    # Dashboard URLs
    path('dashboard/', DashboardPageView.as_view(), name='dashboard'),
    path('dashboard/player/', PlayerDashboardView.as_view(), name='player_dashboard'),
    path('dashboard/coach/', CoachDashboardView.as_view(), name='coach_dashboard'),
    path('dashboard/admin/', AdminDashboardView.as_view(), name='admin_dashboard'),

    # Users URLs
    path('users/', UsersListView.as_view(), name='users'),
    path('users/<int:pk>/', UsersDetailView.as_view(), name='users_detail'),
    path('users/create/', UsersCreateView.as_view(), name='users_create'),
    path('users/<int:pk>/edit/', UsersUpdateView.as_view(), name='users_update'),
    path('users/<int:pk>/delete/', UsersDeleteView.as_view(), name='users_delete'),


    path('position/', PositionListView.as_view(), name='positions'),
    path('position/<int:pk>/', PositionDetailView.as_view(), name='position_detail'),
    path('position/create/', PositionCreateView.as_view(), name='position_create'),
    path('position/<int:pk>/edit/', PositionUpdateView.as_view(), name='position_update'),
    path('position/<int:pk>/delete/',PositionDeleteView.as_view(), name='position_delete'),

    path('matches/', match_list, name='matches_list'),  # URL to match the template


]
