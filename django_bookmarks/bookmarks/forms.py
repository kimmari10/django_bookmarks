from django import forms as forms

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
