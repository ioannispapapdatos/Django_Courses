
from django import forms

from appTwo.models import User



class newUserForm(forms.ModelForm):
    # first_name=forms.CharField(max_length=168)
    class Meta:
        model=User
        fields='__all__'