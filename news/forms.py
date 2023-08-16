from django import forms
from .models import Contact



class ContactsForm(forms.ModelForm):

    class Meta:
        model=Contact
        fields="__all__"
