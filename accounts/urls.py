from django.urls import path
from .views import signup  # Import the signup view
from django.contrib.auth.views import LoginView  # Import the LoginView
from . import views

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', LoginView.as_view(), name='login'),  # Correctly reference the LoginView
    path('user-management/', views.user_management, name='user_management'),
]
