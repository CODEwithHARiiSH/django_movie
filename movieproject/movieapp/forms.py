from django import forms

from .models import movies


class movie_forms(forms.ModelForm):
    class Meta:
        model = movies
        fields = ['name', 'year', 'desc', 'img']
