from django import forms
from django.forms.widgets import EmailInput, Textarea

# Create your forms here.

class ContactForm(forms.Form):
	name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length = 50)
	email_address = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), max_length = 150)
	message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows':'5'}), max_length = 2000)