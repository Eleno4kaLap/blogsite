from django import forms
from .models import EmailSubscriptions


class EmailSubscriptionForm(forms.ModelForm):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={"placeholder": "Email"}))


    class Meta:
        model = EmailSubscriptions
        fields = ['email']