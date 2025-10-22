from django import forms
from .models import Log


class LogForm(forms.ModelForm):
    """
    Form class for users to enter their logs in a category
    """
    class Meta:
        """
        Specify the django model and order of the fields
        """
        model = Log
        fields = ('title', 'content',)
