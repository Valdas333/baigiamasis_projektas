from django.contrib import admin
from .models import Person, Meeting 
# Register your models here.


class PersonAdmin(admin.ModelAdmin):
    list_display = ('name','surname','duties')
    
    
class MeetingAdmin(admin.ModelAdmin):
    list_display = ('title','responsible_person','description')


admin.site.register(Meeting, MeetingAdmin)
admin.site.register(Person, PersonAdmin)