from django import forms
from .models import *
from .date_time_widget import MinimalSplitDateTimeMultiWidget


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


class CreatePersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('name', 'surname', 'duties','email')