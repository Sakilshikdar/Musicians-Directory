# forms.py

from django import forms
from .models import Musician, Album
from django.db import models


class MusicianForm(forms.ModelForm):
    class Meta:
        model = Musician
        fields = ['first_name', 'last_name', 'email',
                  'phone_number', 'instrument_type']


class AlbumForm(forms.ModelForm):
    musician_name = forms.ModelChoiceField(queryset=Musician.objects.all(
    ), label='Musician', to_field_name='id', empty_label=None)

    class Meta:
        model = Album
        fields = ['name', 'musician_name', 'release_date', 'rating']
