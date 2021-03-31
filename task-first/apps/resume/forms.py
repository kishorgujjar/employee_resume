from django import forms

from .models import ResumeItem


class ResumeItemForm(forms.ModelForm):
    """
    A form for creating and editing resume items. Note that 'user' is not
    included: it is always set to the requesting user.
    """
    class Meta:
        model = ResumeItem
        fields = ['title', 'email', 'mobile', 'company', 'designation', 'photo', 'date_of_birth', 'start_date', 'end_date', 'description']
