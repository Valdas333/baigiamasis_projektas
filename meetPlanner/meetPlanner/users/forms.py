from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model, forms as user_forms
from my_planner.models import Person
from django.utils.translation import gettext_lazy as _
User = get_user_model()


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )       


class PersonUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = Person
        fields = ("username", "email", "first_name", "last_name", "duties", "images" )
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
        model = get_user_model()
        fields = ("username", "email", "first_name", "last_name", "images")
        field_classes = {"username": user_forms.UsernameField}

    def clean_email(self):
        email = self.cleaned_data['email']
        username = self.cleaned_data['username']
        user_with_email = get_user_model().objects.filter(email=email).exclude(username=username)
        if not user_with_email.exists():
            return email
        else:
            raise ValidationError(_('User with this email address already exists'))        
