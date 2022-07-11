from django.urls import path

from .views import (CreateMeeting, CreatePerson, DeleteMeeting, DeletePerson,
                    IndexPageListView, MeetingDetailView, PersonDetailView,
                    UpdateMeeting, UpdatePerson, PersonListView)

urlpatterns = [
    path('', IndexPageListView.as_view(),  name='index'),
    path('persons/', PersonListView.as_view(), name='person_list'),
    path('create_meeting/', CreateMeeting.as_view(), name='create_meeting'),
    path('meeting/<int:pk>/', MeetingDetailView.as_view(), name='meeting_detail'),  
    path('meeting/<int:pk>/update_meeting/', UpdateMeeting.as_view(), name='update_meeting'),
    path('meeting/<int:pk>/delete_meeting/', DeleteMeeting.as_view(), name='delete_meeting'),
    path('create_person/', CreatePerson.as_view(), name='create_person'),
    path('person/<int:pk>/', PersonDetailView.as_view(), name='person_detail'),
    path('person/<int:pk>/update_person/', UpdatePerson.as_view(), name='update_person'),
    path('person/<int:pk>/delete_person/', DeletePerson.as_view(), name='delete_person'),        
    ]
