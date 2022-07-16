from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView
from .models import Meeting
from .forms import CreateMeetingForm, UpdateMeetingForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


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
        messages.success(self.request, ("Meeting created successfully, \n details:"))
        return super().form_valid(form)     
    

class UpdateMeeting(LoginRequiredMixin,UpdateView):
    model = Meeting
    form_class = UpdateMeetingForm
    template_name = 'my_planner/update_meeting.html'


class DeleteMeeting(LoginRequiredMixin,DeleteView):
    model = Meeting
    template_name = 'my_planner/delete_meeting_confirm.html' 
    success_url = reverse_lazy('index')