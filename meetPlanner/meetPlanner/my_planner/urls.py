from django.urls import path
from . views import IndexPageListView, MeetingDetailView, CreateMeeting, UpdateMeeting


urlpatterns = [
    path('', IndexPageListView.as_view(),  name='index'),
    path('meeting/<int:pk>/', MeetingDetailView.as_view(), name='meeting_detail'),
    path('create_meeting/', CreateMeeting.as_view(), name='create_meeting'),
    path('meeting/<int:pk>/update_meeting/', UpdateMeeting.as_view(), name='update_meeting')   
    ]
