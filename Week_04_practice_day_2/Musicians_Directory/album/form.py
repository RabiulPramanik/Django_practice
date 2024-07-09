from django import forms
from .models import AlbumModel

class AlbumForm(forms.ModelForm):
    class Meta:
        model = AlbumModel
        fields = ['name','musician','release_date','rating']
        widgets = {
            'release_date': forms.DateInput(attrs={'type': 'date'}),
        }