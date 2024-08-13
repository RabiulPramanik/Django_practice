from django import forms
from .models import AlbumModel

class AlbumForm(forms.ModelForm):
    class Meta:
        model = AlbumModel
        fields = ['Album_Name','Musician','Release_date','Rating']
        widgets = {
            'Release_date': forms.DateInput(attrs={'type': 'date'}),
        }