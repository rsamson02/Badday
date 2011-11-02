from django.db import models
import datetime

class Name(models.Model):
    name = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')
    age = models.CharField(max_length=50)
    
class Foo(models.Model):
    Ticket_Choices = (
        ('Y', 'Yes'),
        ('N', 'No'),
)
    ticket = models.CharField(max_length=1, choices= Ticket_Choices)

class Location(models.Model):
    street = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    state = models.CharField(max_length=250)
    pub_date = models.DateTimeField('date published')
    

class Number_Accidents(models.Model):
    accidents = models.IntegerField(blank=True)
    

