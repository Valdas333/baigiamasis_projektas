from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext_lazy as _
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm, PersonUpdateForm, PersonProfileUpdateForm, ExtendedUserUpdateForm, UserProfileUpdateForm, UserProfileForm
from my_planner.models import Person  
    

class UserCreate(CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('index')
    template_name = 'users/register.html'


class PersonListView(ListView):
    model = User
    template_name = 'my_planner/persons_list.html'
    context_object_name = 'persons'    
    paginate_by = 9  
    
    
class ProfileDetailView(DetailView):
    model = User
    template_name = 'users/person_detail.html'
  
   
class UpdatePerson(LoginRequiredMixin, UpdateView):
    model = User
    form_class = PersonUpdateForm
    success_url = reverse_lazy('index')
    template_name = 'users/register.html'

    def form_valid(self, form):
        messages.success(self.request,  _("User data has been updated successfully"))
        return super().form_valid(form)    
    
        
class DeletePerson(LoginRequiredMixin, DeleteView):
    model = User
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
def create_person(request):
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


@login_required()
def editUserProfile(request, pk):
    user_form  = User.objects.get(id = pk)
    profile_form= Person.objects.get(user_id = pk)
    if request.method == "POST":
        form = UserProfileUpdateForm(request.POST, request.FILES, instance=user_form)
        form1 = UserProfileForm(request.POST, instance=profile_form)
        if form.is_valid() and form1.is_valid():
            form.save()
            form1.save()
            messages.success(request, f'updated successfully')
            return redirect('index')
        else:
            messages.error(request, f'Please correct the error below.')
    else:
        form = UserProfileUpdateForm(request.POST, request.FILES, instance=user_form)
        form1 = UserProfileForm(request.POST,  instance=profile_form)
             
    return render(request, "users/update_person.html", {'form': form, 'form1': form1})