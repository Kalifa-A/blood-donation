from django.db import models
from django import forms
from datetime import datetime

class RegistrationForm(models.Model):

    BLOOD_GROUPS = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('A1B+','A1B+'),
        ('A1B-','A1B-'),
        ('A2B+','A2B+'),
         ('A2B-','A2B-')
    ]
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    bloodgroup = models.CharField(max_length=100,choices=BLOOD_GROUPS)
    native = models.CharField(max_length=100)
    contact = models.CharField(max_length=50)
    email=models.EmailField()
    date_remain = models.DurationField(default=None, editable=False)
    donated_date = models.CharField(max_length=20)

    class Meta:
        db_table = 'data'




    def save(self, *args, **kwargs):
        if self.donated_date:
            user_input_date = datetime.strptime(self.donated_date, "%Y-%m-%d")
            current_date = datetime.now()
            date_difference = current_date - user_input_date
            self.date_remain = date_difference
        super().save(*args, **kwargs)

    def calculate_date_remain(self):
        if self.donated_date:
            user_input_date = datetime.strptime(self.donated_date, "%Y-%m-%d")
            current_date = datetime.now()
            date_difference = current_date - user_input_date
            return date_difference.days
        return None

    def __str__(self):
        return f"{self.date_remain}"
