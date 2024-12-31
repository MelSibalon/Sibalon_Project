from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Sport

class HomePageView(TemplateView):
    template_name = 'app/home.html'

class AboutPageView(TemplateView):
    template_name = 'app/about.html'

class MsListView(ListView):
    template_name = 'app/ms_list.html'
    model = Sport
    context_object_name = 'sports'

class MsDetailView(DetailView):
    template_name = 'app/ms_detail.html'
    model = Sport
    context_object_name ='sport'


class MsCreateView(CreateView):
    template_name = 'app/ms_create.html'
    model = Sport
    fields = ['sport_name', 'description', 'rules']

class MsUpdateView(UpdateView):
    template_name = 'app/ms_update.html'
    model = Sport
    fields = ['sport_name', 'description', 'rules']

class MsDeleteView(DeleteView):
    template_name = 'app/ms_delete.html'
    model = Sport
    success_url = reverse_lazy('ms')