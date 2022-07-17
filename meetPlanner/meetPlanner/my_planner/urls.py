from django.urls import path
from .views import (CreateMeeting, DeleteMeeting,
                    IndexPageListView, MeetingDetailView,
                    UpdateMeeting)



urlpatterns = [
    path('', IndexPageListView.as_view(),  name='index'),
    path('create_meeting/', CreateMeeting.as_view(), name='create_meeting'),
    path('meeting/<int:pk>/', MeetingDetailView.as_view(), name='meeting_detail'),  
    path('meeting/<int:pk>/update_meeting/', UpdateMeeting.as_view(), name='update_meeting'),
    path('meeting/<int:pk>/delete_meeting/', DeleteMeeting.as_view(), name='delete_meeting'),
  
    ]
