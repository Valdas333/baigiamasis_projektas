from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField('Vardas', max_length=100)
    surname = models.CharField('Pavarde', max_length=100)
    duties = models.CharField('Pareigos', max_length=20)
    email = models.EmailField('Elektroninis pastas', max_length=254, blank=False)
    
    def __str__(self):
        return f"Atsakingas asmuo {self.name} {self.surname}"
    
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
    start_time = models.TimeField(auto_now=True, blank=False, error_messages= "Pasirinkite tinkama pradzios laika")
    start_date = models.DateField(auto_now=True, blank=False)
    end_time = models.TimeField(auto_now=False, blank=False)
    end_date = models.DateField(auto_now=False, blank=False)