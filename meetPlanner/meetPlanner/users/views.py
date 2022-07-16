from django.contrib import messages
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from .forms import UserRegisterForm, PersonUpdateForm, PersonProfileUpdateForm
from django.urls import reverse_lazy
User = get_user_model()
from my_planner.models import Person
from django.contrib.auth.mixins import LoginRequiredMixin


class UserCreate(CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('index')
    template_name = 'users/register.html'


class PersonListView(ListView):
    model = Person
    template_name = 'my_planner/persons_list.html'
    context_object_name = 'persons'    
    paginate_by = 3   
    
class ProfileDetailView(DetailView):
    model = Person
    template_name = 'users/person_detail.html'


class CreatePerson(LoginRequiredMixin, CreateView):
    form_class = UserRegisterForm
    template_name = 'users/create_person.html'
    success_url = reverse_lazy('person_list')
   
   
class UpdatePerson(LoginRequiredMixin, UpdateView):
    model = Person
    form_class = PersonUpdateForm
    success_url = reverse_lazy('index')
    template_name = 'users/register.html'

    def form_valid(self, form):
        messages.success(self.request,  ("User data has been updated successfully"))
        return super().form_valid(form)    
    
        
class DeletePerson(LoginRequiredMixin, DeleteView):
    model = Person
    template_name = 'users/delete_person_confirm.html' 
    success_url = reverse_lazy('person_list')
    

class UpdatePersonProfile(LoginRequiredMixin, UpdateView):
    form_class = PersonProfileUpdateForm
    success_url = reverse_lazy('index')
    template_name = 'users/update_person.html'
    queryset = get_user_model().objects.all()

    def get_object(self, queryset=get_user_model().objects.all()):
        return queryset.get(pk=self.request.user.pk)

    def form_valid(self, form):
        messages.success(self.request, ("User data has been updated successfully"))
        return super().form_valid(form)       
