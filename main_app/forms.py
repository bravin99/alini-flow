from django import forms
from main_app.models import Contact, ServiceRequest


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'email', 'phone', 'message', 'call_back']


class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['full_name', 'phone_number', 'email', 'message', 'call_back']
