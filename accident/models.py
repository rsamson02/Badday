from django.db import models
import datetime

class AccidentType(models.Model):
    accident_type = models.CharField(max_length=255)
    def __unicode__(self):
        return self.accident_type
    def get_absolute_url(self):
        return "accident-types/%i/" % self.id

class VehicleType(models.Model):
    vehicle_type = models.CharField(max_length=255)
    def __unicode__(self):
        return self.vehicle_type
    def get_absolute_url(self):
        return "vehicle-types/%i/" % self.id
    
class Accident(models.Model):
    street = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    state = models.CharField(max_length=250)
    pub_date = models.DateTimeField('date published')
    accident_type = models.ForeignKey(AccidentType)
    vehicle_type = models.ManyToManyField(VehicleType)
    ticket_issued = models.BooleanField()
    def get_absolute_url(self):
        return "/accident/%i/"% self.id
