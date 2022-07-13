from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.utils import timezone
import datetime

class Person(models.Model):
    name = models.CharField('Name', max_length=100, blank=False)
    surname = models.CharField('Surname', max_length=100, blank=False)
    DUTIES_FIXED_VALUES = [
        ('a', 'Developer'),
        ('b', 'Support'),
        ('c', 'Testing'),
        ('d', 'Management'),
    ]
    duties = models.CharField('Duties', choices= DUTIES_FIXED_VALUES, blank=False, max_length=50)
    email = models.EmailField('Email', max_length=254, blank=False)
    
    def __str__(self):
        return f"{self.name} {self.surname} {self.get_duties_display()}"
    
    
class Meeting(models.Model):
    title = models.CharField('Title', max_length=10)
    responsible_person = models.ForeignKey(to='Person', verbose_name='Responsible person', on_delete=models.SET_NULL, null=True)
    description = models.CharField('Aprasymas', max_length=50, help_text='Description about 50 simbols')
    CATEGORY_FIXED_VALUES = [
        ('a', 'CodeMonkey'),
        ('b', 'Hub'),
        ('c', 'Short'),
        ('d', 'TeamBuilding'),
    ]
    category = models.CharField(max_length=1, choices= CATEGORY_FIXED_VALUES, blank=True, default='a', help_text='Category')
    TYPE_FIXED_VALUES = [
        ('a', 'Live'),
        ('b', 'InPerson'),
    ]
    type = models.CharField(max_length=1, choices = TYPE_FIXED_VALUES, blank=False,)
    start_time = models.DateTimeField(blank=False)
    end_time = models.DateTimeField(blank=False)
    create_time = models.DateTimeField(auto_now_add=True, editable=False)

    def clean(self):
        if self.start_time < timezone.now():
            raise ValidationError({'start_time': 'The date cannot be in the past!'})
        if self.start_time >= self.end_time:
            raise ValidationError({'end_time': 'The end time cannot be earler or equal than start time'})  
           
    def __str__(self):
        return f"Meet {self.title} is scheduled from {self.start_time} until {self.end_time}, created @{self.create_time}"
    
    def meeting_duration(self):
        duration = self.end_time - self.start_time
        return int(duration.total_seconds()/60)
        
    
    def get_absolute_url(self):
        return reverse('meeting_detail', kwargs={'pk':self.pk})

    