from django import forms
from .models import Person, Meeting
from .date_time_widget import MinimalSplitDateTimeMultiWidget
from django.contrib.auth.forms import UserCreationForm, UserChangeForm



class CreateMeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = ('title', 'description', 'category', 'type', 'start_time', 'end_time', 'responsible_person')
        widgets = {
            'start_time': MinimalSplitDateTimeMultiWidget(),
            'end_time': MinimalSplitDateTimeMultiWidget(),
        }
        

class UpdateMeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = ('title', 'description', 'category', 'type', 'start_time', 'end_time', 'responsible_person')
        widgets = {
            'start_time': MinimalSplitDateTimeMultiWidget(),
            'end_time': MinimalSplitDateTimeMultiWidget(),
            }


# class CreatePersonForm(forms.ModelForm):
#     # class Meta:
#     #     model = Person
#     #     fields = ('name', 'surname', 'duties','email')
#     class Meta:
#         model = Person
#         fields = '__all__'
        
class PersonCreationForm(UserCreationForm):
    class Meta:
        model = Person
        fields = '__all__'
        

        
        


