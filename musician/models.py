# models.py

from django.db import models
from django.contrib.auth.models import User


class Musician(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    instrument_type = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Album(models.Model):
    name = models.CharField(max_length=200)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    release_date = models.DateField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
