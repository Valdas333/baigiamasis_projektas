from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView

class IndexPageView(TemplateView):
    
    template_name = 'my_planner/index.html'




    