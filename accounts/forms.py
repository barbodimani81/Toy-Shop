from django import forms

from .models import User


class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                "Username is already taken. Please choose another username"
            )
        return username

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email exist!")
        return email

    def clean_password_2(self):
        password_2 = self.cleaned_data["password_2"]
        password_1 = self.cleaned_data["password_1"]
        if password_2 != password_1:
            raise forms.ValidationError("passwords are not the same!")
        return password_1
