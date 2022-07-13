from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView
from .models import Meeting, Person
from .forms import CreateMeetingForm, UpdateMeetingForm, CreatePersonForm, UpdatePersonForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin



class IndexPageListView(ListView):
    model = Meeting
    template_name = 'my_planner/index.html'
    context_object_name = 'meetings'
    

class MeetingDetailView(DetailView):
    model = Meeting
    

class CreateMeeting(LoginRequiredMixin, CreateView): 
    form_class = CreateMeetingForm
    template_name = 'my_planner/create_meeting.html'
    # success_url = reverse_lazy('create_meeting')
    

class UpdateMeeting(LoginRequiredMixin,UpdateView):
    model = Meeting
    form_class = UpdateMeetingForm
    template_name = 'my_planner/update_meeting.html'


class DeleteMeeting(LoginRequiredMixin,DeleteView):
    model = Meeting
    template_name = 'my_planner/delete_meeting_confirm.html' 
    success_url = reverse_lazy('index')


class PersonListView(ListView):
    model = Person
    template_name = 'my_planner/persons_list.html'
    context_object_name = 'persons'    


class CreatePerson(LoginRequiredMixin, CreateView):
    model = Person
    form_class = CreatePersonForm
    template_name = 'my_planner/create_person.html'
    success_url = reverse_lazy('person_list')
    
    
class PersonDetailView(DetailView):
    model = Person


class UpdatePerson(LoginRequiredMixin, UpdateView):
    model = Person
    form_class = UpdatePersonForm
    template_name = 'my_planner/update_person.html'
    success_url = reverse_lazy('person_list')
    

class DeletePerson(LoginRequiredMixin, DeleteView):
    model = Person
    template_name = 'my_planner/delete_person_confirm.html' 
    success_url = reverse_lazy('person_list')