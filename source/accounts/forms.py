from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        label='Login'
    )
    password = forms.CharField(
        required=True,
        label='Password',
        widget=forms.PasswordInput
    )
    next = forms.CharField(
        required=False,
        widget=forms.HiddenInput
    )


class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(
        label='Password',
        strip=False,
        required=True,
        widget=forms.PasswordInput
    )
    password_confirm = forms.CharField(
        label='Confirm password',
        strip=False,
        required=True,
        widget=forms.PasswordInput
    )

    class Meta:
        model = get_user_model()
        fields = (
            'username',
            'email',
            'avatar',
            'password',
            'password_confirm',
            'first_name',
            'about_user',
            'phone_number',
            'gender'
        )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise ValidationError('Password dont match')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        # user.groups.add('user')
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('username',
                  'email',
                  'avatar',
                  'first_name',
                  'about_user',
                  'phone_number',
                  'gender'
                  )
        labels = {'username': 'Username',
                  'email': 'Email',
                  'avatar': 'Profile photo',
                  'first_name': 'Name',
                  'about_user': 'About',
                  'phone_number': 'Phone number',
                  'gender': 'Gender'
                  }


class PasswordChangeForm(forms.ModelForm):
    password = forms.CharField(label="New password", strip=False, widget=forms.PasswordInput)
    password_confirm = forms.CharField(label="Confirm password", widget=forms.PasswordInput, strip=False)
    old_password = forms.CharField(label="Old password", strip=False, widget=forms.PasswordInput)

    def clean_password_confirm(self):
        password = self.cleaned_data.get("password")
        password_confirm = self.cleaned_data.get("password_confirm")
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Password dont match!')
        return password_confirm

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')
        if not self.instance.check_password(old_password):
            raise forms.ValidationError('Old password incorrect!')
        return old_password

    def save(self, commit=True):
        user = self.instance
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ['password', 'password_confirm', 'old_password']
