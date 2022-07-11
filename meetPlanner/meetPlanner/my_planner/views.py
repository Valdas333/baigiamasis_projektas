from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView
from .models import Meeting, Person
from .forms import CreateMeetingForm, UpdateMeetingForm, CreatePersonForm
from django.urls import reverse_lazy, reverse


class IndexPageListView(ListView):
    model = Meeting
    template_name = 'my_planner/index.html'
    context_object_name = 'meetings'


class MeetingDetailView(DetailView):
    model = Meeting
    
 
class CreateMeeting(CreateView): 
    form_class = CreateMeetingForm
    template_name = 'my_planner/create_meeting.html'
    # success_url = reverse_lazy('create_meeting')
    
    
class UpdateMeeting(UpdateView):
    model = Meeting
    form_class = UpdateMeetingForm
    template_name = 'my_planner/update_meeting.html'


class DeleteMeeting(DeleteView):
    model = Meeting
    template_name = 'my_planner/delete_meeting_confirm.html' 
    success_url = reverse_lazy('index')


class CreatePerson(CreateView):
    model = Person
    form_class = CreatePersonForm
    template_name = 'my_planner/create_person.html'
    success_url = reverse_lazy('index')
    