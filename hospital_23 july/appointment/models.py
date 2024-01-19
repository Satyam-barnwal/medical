from django.db import models
import datetime
# Create your models here.


my_choice = (
                     ('Jayesh Sharma', 'Jayesh Sharma'),
                     ('Gaurav Gupta', 'Gaurav Gupta'),
                     ('Ashish Mazumdar','Ashish Mazumdar'),
                     ('Sandip Ojha','Sandip Ojha'),
                     ('Harsha KN','Harsha KN'),
                     ('Manisha Sahu','Manisha Sahu'),
                     ('Jay Rai','Jay Rai'),
                 )
slot_tup = (
    ('Slot1', '10:00-12:00'),
    ('Slot2','12:00-2:00'),
    ('Slot3','2:00-4:00'),
    ('Slot4','4:00-6:00'),

)
class Doctor(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField()
    exp = models.IntegerField()


class holidaytime(models.Model):
    holiday_date = models.DateField()

class Patient(models.Model):
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    mob_no = models.CharField(max_length=12)
    email = models.EmailField()

class AppointmentDetails(models.Model):
    name = models.CharField(max_length=50)
    mob_no = models.CharField(max_length=50)
    email = models.EmailField()
    consultant = models.CharField(max_length=50, choices=my_choice)  # we need to fetch data from doctor table
    date = models.DateField()
    slot = models.CharField(max_length=50, choices= slot_tup)

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    message = models.TextField(max_length=50)

