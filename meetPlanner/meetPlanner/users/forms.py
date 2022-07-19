from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model, forms as user_forms
from django.utils.translation import gettext_lazy as _




from my_planner.models import Person


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')  


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
   
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'password1', 'password2', )       


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
        fields = '__all__'
        # fields = ("username", "email", "first_name", "last_name", )
        field_classes = {"username": user_forms.UsernameField}

    def clean_email(self):
        email = self.cleaned_data['email']
        username = self.cleaned_data['username']
        user_with_email = get_user_model().objects.filter(email=email).exclude(username=username)
        if not user_with_email.exists():
            return email
        else:
            raise ValidationError(_('User with this email address already exists'))        


class PersonUserUpdateForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'


class ExtendedUserUpdateForm(UserCreationForm):  
    class Meta:
        model = User
        fields = ('email', 'username', )       
       
    
class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__' 




    
