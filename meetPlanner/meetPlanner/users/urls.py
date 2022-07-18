from django.urls import path
from .views import UserCreate, PersonListView, ProfileDetailView, DeletePerson, UpdatePerson, UpdatePersonProfile, update_person_profile


urlpatterns = [

    path('persons/', PersonListView.as_view(), name='person_list'),
    path('person/<int:pk>', ProfileDetailView.as_view(), name='person_detail'),
    path('person/<int:pk>/update_person/', UpdatePerson.as_view(), name='update_person'),
    path('person/<int:pk>/delete_person/', DeletePerson.as_view(), name='delete_person'),
    path('person/<int:pk>/update_profile/', UpdatePersonProfile.as_view(), name='update_person_profile'),
    path('create_person/', update_person_profile, name='create_person'),    
]