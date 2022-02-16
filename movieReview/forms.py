from django import forms
from django.db import models
from django.db.models import fields

from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'