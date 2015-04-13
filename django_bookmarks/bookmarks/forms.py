from django import forms as forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

class RegistrationForm(forms.Form):
 username = forms.CharField(label='username', max_length=30)
 email = forms.EmailField(label='email')
 password1 = forms.CharField(
  label='password',
  widget=forms.PasswordInput()
 )

 password2 = forms.CharField(
  label='password(verify)',
  widget=forms.PasswordInput()
 )
 
 def clean_password2(self):
  if 'password1' in self.cleaned_data:
   password1 = self.cleaned_data['password1']
   password2 = self.cleaned_data['password2']
   if password1 == password2:
    return password2
  raise forms.ValidationError('invalid password')

 def clean_username(self):
  username = self.cleaned_data['username']
  if not re.search(r'^\w+$', username):
   raise forms.ValidationError(' Alphabet, number, _ only')
  try:
   User.objects.get(username=username)
  except ObjectDoesNotExist:
   return username
  raise forms.ValidationError('already exist ID')


class BookmarkSaveForm(forms.Form):
 url = forms.URLField(
  label = 'address',
  widget = forms.TextInput(attrs={'size':64})
 )

 title = forms.CharField(
  label = 'title',
  widget = forms.TextInput(attrs={'size':64})
 )

 tags = forms.CharField(
  label = 'tag',
  required=False,
  widget = forms.TextInput(attrs={'size':64})
 )




class SearchForm(forms.Form):
 query = forms.CharField(
  label='type keword',
  widget=forms.TextInput(attrs={'size':32})
 )
