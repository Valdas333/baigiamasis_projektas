from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView, TemplateView
from .forms import CreateMeetingForm, UpdateMeetingForm, MeetingEventForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.shortcuts import render, redirect
from .models import Meeting, MeetingEvent
from django.contrib.auth import get_user_model

class MeetingEventList(ListView):
    model = MeetingEvent
    template_name = 'my_planner/index.html'
    context_object_name = 'meetings'


class IndexPageListView(ListView):
    model = Meeting
    template_name = 'my_planner/index.html'
    context_object_name = 'meetings'
    paginate_by = 3    


class MeetingDetailView(DetailView):
    model = Meeting
    

class CreateMeeting(LoginRequiredMixin, CreateView): 
    form_class = CreateMeetingForm
    template_name = 'my_planner/create_meeting.html'
    
    def form_valid(self, form):
        messages.success(self.request, (_("Meeting created successfully")))
        return super().form_valid(form)     
    

class UpdateMeeting(LoginRequiredMixin,UpdateView):
    model = Meeting
    form_class = UpdateMeetingForm
    template_name = 'my_planner/update_meeting.html'


class DeleteMeeting(LoginRequiredMixin,DeleteView):
    model = Meeting
    template_name = 'my_planner/delete_meeting_confirm.html' 
    success_url = reverse_lazy('index')
    
    

def add_meeting_event(request):
    if request.method == 'POST':
        meeting_form = CreateMeetingForm(request.POST)
        participant_form = MeetingEventForm(request.POST)
        
        if meeting_form.is_valid() and participant_form.is_valid():
            meeting = meeting_form.save(commit=False)
            participant = participant_form.save(commit=False)

            meeting.save()
            participant.meeting_id = meeting.id
            participant.save() 
            return redirect('person_list')

    else:
        meeting_form = CreateMeetingForm()
        participant_form = MeetingEventForm()
        
    context = {
        'meeting_form': meeting_form,
        'participant_form': participant_form,
    }
    return render(request, 'my_planner/create_meeting_event.html', context)

            
def user_meeting_filter(request):
    user = request.user.id 
    all_events = MeetingEvent.objects.all()
    user_event = all_events.filter(participant_id = user) 
    print(user_event)
    all_meetings = Meeting.objects.all()
    context = {'events': user_event,
               'meetings': all_meetings,}
    return render(request, 'my_planner/user_events.html', context)
            
            