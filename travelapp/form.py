from django import forms

from . models import place
class ModeForm(forms.ModelForm):
    class Meta:
        model=place
        fields=['name','desc','price','img']

