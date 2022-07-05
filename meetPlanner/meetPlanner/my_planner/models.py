from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField('Vardas', max_length=100, blank=False)
    surname = models.CharField('Pavarde', max_length=100, blank=False)
    DUTIES_FIXED_VALUES = [
        ('a', 'Developer'),
        ('b', 'Support'),
        ('c', 'Testing'),
        ('d', 'Management'),
    ]
    duties = models.CharField('Pareigos', choices= DUTIES_FIXED_VALUES, blank=False, max_length=50)
    email = models.EmailField('Elektroninis pastas', max_length=254, blank=False)
    
    def __str__(self):
        return f"{self.name} {self.surname} {self.get_duties_display()}"
    
class Meeting(models.Model):
    title = models.CharField('Title', max_length=10)
    responsible_person = models.ForeignKey(to='Person', verbose_name='Atsakingas asmuo', on_delete=models.SET_NULL, null=True)
    description = models.CharField('Aprasymas', max_length=50, help_text='trumpas aprasymas, apie 50 simboliu')
    CATEGORY_FIXED_VALUES = [
        ('a', 'CodeMonkey'),
        ('b', 'Hub'),
        ('c', 'Short'),
        ('d', 'TeamBuilding'),
    ]
    category = models.CharField(max_length=1, choices= CATEGORY_FIXED_VALUES, blank=True, default='a', help_text='kategorija')
    TYPE_FIXED_VALUES = [
        ('a', 'Live'),
        ('b', 'InPerson'),
    ]
    type = models.CharField(max_length=1, choices = TYPE_FIXED_VALUES, blank=False,)
    start_time = models.DateTimeField(auto_now=True, blank=False)
    end_time = models.DateTimeField(blank=False)
    create_time = models.DateTimeField(auto_now_add=True, editable=False)
    
    def __str__(self):
        return f"Meetas {self.title}, paskirtas laikas nuo {self.start_time} iki {self.end_time}, sukurtas {self.create_time}"