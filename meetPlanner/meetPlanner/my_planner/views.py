from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DetailView
from .models import Meeting
from .forms import CreateMeetingForm
from django.views.generic.edit import FormView
from django.urls import reverse_lazy


class IndexPageListView(ListView):
    model = Meeting
    template_name = 'my_planner/index.html'
    context_object_name = 'meetings'


class MeetingListView(DetailView):
    model = Meeting
    template_name = 'my_planner/meeting.html'
    context_object_name = 'meeting'


class CreateMeeting(CreateView):
    
    form_class = CreateMeetingForm
    template_name = 'my_planner/create_meeting.html'
    success_url = reverse_lazy('create_meeting')
    