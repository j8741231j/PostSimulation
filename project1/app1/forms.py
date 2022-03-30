from django import forms
from .models import *

class UploadModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('image',)
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control-file' ,'id':'image'})
        }