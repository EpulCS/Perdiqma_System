from django import forms
from .models import Activity, GalleryPicture

class PinForm(forms.Form):
    pin = forms.CharField(widget=forms.PasswordInput, max_length=6)

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['title', 'description', 'date', 'members', 'picture']

class PictureForm(forms.ModelForm):
    class Meta:
        model = GalleryPicture
        fields = ['image', 'caption']