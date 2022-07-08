from django.urls import path
from . views import IndexPageListView

urlpatterns = [
    path('', IndexPageListView.as_view(),  name='index'),
    
    ]
