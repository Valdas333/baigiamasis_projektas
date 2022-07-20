from django import forms
from .models import Meeting
from .date_time_widget import MinimalSplitDateTimeMultiWidget
from my_planner.models import MeetingEvent


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

        
class MeetingEventForm(forms.ModelForm):
    class Meta:
        model = MeetingEvent
        fields = ("participant",)
            
        

