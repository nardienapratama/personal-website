from django.db import models
from django.utils import timezone
from datetime import datetime, date

# Create your models here.

class Schedule(models.Model):
    eventName = models.CharField(max_length=50)
    date = models.DateField(default=timezone.now)
    time = models.TimeField(default=timezone.now)
    category = models.CharField(max_length=50)
    location = models.CharField(max_length=50)

    @classmethod
    def create(cls, eventName, date, time, category, location):
        schedule = cls(eventName=eventName, date=date, time=time, category=category, location=location)
        return schedule

class Registration(models.Model):
    firstname = models.CharField(max_length = 50)
    lastname = models.CharField(max_length = 50)
    username = models.CharField(max_length=50)
    email = models.CharField(max_length = 50, unique=True)
    password = models.CharField(max_length = 50)

    @classmethod
    def create(cls, firstname, lastname, username, email, password):
        registration = cls(firstname=firstname, lastname=lastname, username=username, email=email, password=password)
        return registration
