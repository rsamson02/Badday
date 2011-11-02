from django.db import models
import datetime

class Accident(models.Model):
    Type = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')


