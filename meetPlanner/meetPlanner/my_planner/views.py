from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, UpdateView, CreateView
from .models import Meeting


class IndexPageListView(ListView):
    model = Meeting
    template_name = 'my_planner/index.html'
    context_object_name = 'meetings'


# class CreateMeeting(CreateView):
#     model = Meeting
#     fields = 
    