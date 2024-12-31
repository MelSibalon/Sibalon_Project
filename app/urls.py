from django.urls import path
from .views import (HomePageView, AboutPageView, MsListView, 
                    MsDetailView, MsCreateView, MsUpdateView, MsDeleteView)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('ms/', MsListView.as_view(), name='ms'),
    path('ms/<int:pk>', MsDetailView.as_view(), name='ms_detail'),
    path('ms/create', MsCreateView.as_view(), name='ms_create'),
    path('ms/<int:pk>/edit', MsUpdateView.as_view(), name='ms_update'),
    path('ms/<int:pk>/delete', MsDeleteView.as_view(), name='ms_delete'),
]