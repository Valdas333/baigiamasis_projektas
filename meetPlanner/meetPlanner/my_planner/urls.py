from django.urls import path
from . views import IndexPageListView,MeetingListView, CreateMeeting

urlpatterns = [
    path('', IndexPageListView.as_view(),  name='index'),
    path('meeting/<int:meeting_id>/',MeetingListView.as_view(), name='meeting'),
    path('create_meeting/', CreateMeeting.as_view(), name='create_meeting'),   
    ]
