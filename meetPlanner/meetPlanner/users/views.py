from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView, TemplateView
from .forms import UserRegisterForm, PersonUpdateForm, PersonProfileUpdateForm, ExtendedUserUpdateForm, UserProfileUpdateForm
from django.urls import reverse_lazy
from my_planner.models import Person
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext_lazy as _
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from my_planner.models import Person

class UserCreate(CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('index')
    template_name = 'users/register.html'


class PersonListView(ListView):
    model = User
    template_name = 'my_planner/persons_list.html'
    context_object_name = 'persons'    
    paginate_by = 3   
    
class ProfileDetailView(DetailView):
    model = Person
    template_name = 'users/person_detail.html'


# class CreatePerson(LoginRequiredMixin, CreateView):
#     form_class = UserRegisterForm
#     template_name = 'users/create_person.html'
#     success_url = reverse_lazy('person_list')
   
   
class UpdatePerson(LoginRequiredMixin, UpdateView):
    model = User
    form_class = PersonUpdateForm
    success_url = reverse_lazy('index')
    template_name = 'users/register.html'

    def form_valid(self, form):
        messages.success(self.request,  _("User data has been updated successfully"))
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
        messages.success(self.request, _("User data has been updated successfully"))
        return super().form_valid(form)       
    
    
@login_required
def update_person_profile(request):
    if request.method == "POST":
        user_form = ExtendedUserUpdateForm(request.POST)
        profile_form = UserProfileUpdateForm(request.POST, request.FILES)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()           
            messages.success(request, f"Profilis atnaujintas")
            return redirect('person_list')
    else:
        user_form = ExtendedUserUpdateForm(request.POST)
        profile_form = UserProfileUpdateForm(request.POST, request.FILES)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'users/register.html', context)