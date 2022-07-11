from django import forms 
from .models import (BlogPost, ContactDb, JoinDb)


class BlogForm(forms.ModelForm):
	class Meta:
		model=BlogPost
		fields=['title', 'body', 'image']

class ContactForm(forms.ModelForm):
	email_address= forms.CharField(widget=forms.TextInput(attrs={"placeholder":"@example.com"}))
	class Meta:
		model=ContactDb
		fields=['first_name', 'last_name', 'email_address','message']


class JoinForm(forms.ModelForm):
	email_address= forms.CharField(widget=forms.TextInput(attrs={"placeholder":"@example.com"}))
	DOB=forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))

	class Meta:
		model=JoinDb
		fields=['first_name', 'last_name', 'email_address',"seg_id",'affilate_uni', 'DOB']


