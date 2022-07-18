from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model, forms as user_forms
from my_planner.models import Person
from django.utils.translation import gettext_lazy as _


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:

        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )       


class PersonUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User

        fields = ("username", "email", "first_name", "last_name", )
        field_classes = {"username": user_forms.UsernameField}

    def clean_email(self):
        email = self.cleaned_data['email']
        username = self.cleaned_data['username']
        user_with_email = get_user_model().objects.filter(email=email).exclude(username=username)
        if not user_with_email.exists():
            return email
        else:
            raise ValidationError(_('User with this email address already exists'))
        

class PersonProfileUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User

        fields = ("username", "email", "first_name", "last_name", )
        field_classes = {"username": user_forms.UsernameField}

    def clean_email(self):
        email = self.cleaned_data['email']
        username = self.cleaned_data['username']
        user_with_email = get_user_model().objects.filter(email=email).exclude(username=username)
        if not user_with_email.exists():
            return email
        else:
            raise ValidationError(_('User with this email address already exists'))        


class ExtendedUserUpdateForm(UserCreationForm):  
    class Meta:
        model = User
        fields = ('email', 'username', )
        
    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     user.email = self.cleaned_data['email'] 
         
    
class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('images', )


        