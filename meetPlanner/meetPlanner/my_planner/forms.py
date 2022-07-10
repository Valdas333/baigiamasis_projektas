from django import forms
from .models import *


class CreateMeetingForm(forms.Form):
    class Meta:
        model = Meeting
        fields = ('title', 'description', 'category', 'type', 'start_time', 'end_time', 'responsible_person')