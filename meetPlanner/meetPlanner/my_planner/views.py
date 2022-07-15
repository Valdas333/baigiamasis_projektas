from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView
from .models import Meeting
from .forms import CreateMeetingForm, UpdateMeetingForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User




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





# def create_person(request, pk):
#     user_profile = Person.objects.get(pk=id) 
#     UserFormSet = inlineformset_factory(User, Person, fields = ('name', 'surname'))
#     formset = UserFormSet(instance = user_profile)
#     if request.method == 'POST':
#         form = CreatePersonForm(request.POST)
#         if form.is_valid():
#             form.save
#             return redirect('/')
        
#     context = {'formset': formset}
#     return render(request, 'my_planner/create_person.html', context)
    

            
