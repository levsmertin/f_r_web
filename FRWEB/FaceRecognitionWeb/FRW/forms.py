from django import forms
from FRW.models import PhotoBase

class PhotoBaseForm(forms.ModelForm):
    class Meta:
        model = PhotoBase
        fields = ('photo','text1',)
