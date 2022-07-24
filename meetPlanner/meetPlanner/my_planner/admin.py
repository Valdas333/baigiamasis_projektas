from django.contrib import admin
from .models import Person, Meeting, MeetingEvent


class PersonAdmin(admin.ModelAdmin):
    list_display = ('duties',)
    
    
class MeetingAdmin(admin.ModelAdmin):
    list_display = ('title','responsible_person','description',)


class MeetingEventAdmin(admin.ModelAdmin):
    list_display = ('participant', 'meeting',)


admin.site.register(Meeting, MeetingAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(MeetingEvent, MeetingEventAdmin)


