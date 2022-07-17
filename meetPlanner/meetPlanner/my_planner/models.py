from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class Person(AbstractUser):
    DUTIES_FIXED_VALUES = (
        (0, _('Developer')),
        (10, _('Support')),
        (11, _('Testing')),
        (20, _('Management')),
    )
    duties = models.CharField(_('Duties'), choices= DUTIES_FIXED_VALUES, blank=True, max_length=50)
    images = models.ImageField(_('Images'), default='default.jpg', upload_to='profile_pics')
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.get_duties_display()}"

    class Meta:
        verbose_name = _('Person')
        verbose_name_plural = _('Persons')
    
    
class Meeting(models.Model):
    title = models.CharField(_('Title'), max_length=10)
    responsible_person = models.ForeignKey(to='Person', verbose_name=_('Responsible person'), on_delete=models.SET_NULL, null=True)
    description = models.CharField(_('Description'), max_length=50, help_text=_('Description about 50 simbols'))
    CATEGORY_FIXED_VALUES = (
        (0, 'CodeMonkey'),
        (10, 'Hub'),
        (11, 'Short'),
        (20, 'TeamBuilding'),
    )
    category = models.CharField(_('Category'), max_length=1, choices= CATEGORY_FIXED_VALUES, blank=True, default='a', help_text=_('Category'))
    TYPE_FIXED_VALUES = (
        (0, _('Live')),
        (1, _('InPerson')),
    )
    type = models.CharField(_('Type'), max_length=1, choices = TYPE_FIXED_VALUES, blank=False,)
    start_time = models.DateTimeField(_('Meeting start time'), blank=False)
    end_time = models.DateTimeField(_('Meeting end time'),blank=False)
    create_time = models.DateTimeField(_('Meeting create time'), auto_now_add=True, editable=False)

    def clean(self):
        if self.start_time < timezone.now():
            raise ValidationError({'start_time': _('The date cannot be in the past!')})
        if self.start_time >= self.end_time:
            raise ValidationError({'end_time': _('The end time cannot be earler or equal than start time')})  
           
    def __str__(self):
        return f"Meet {self.title} is scheduled from {self.start_time} until {self.end_time}, created @{self.create_time}"
    
    def meeting_duration(self):
        duration = self.end_time - self.start_time
        return int(duration.total_seconds()/60)
           
    def get_absolute_url(self):
        return reverse('meeting_detail', kwargs={'pk':self.pk})

    class Meta:
        verbose_name = _('Meeting')
        verbose_name_plural = _('Meetings')