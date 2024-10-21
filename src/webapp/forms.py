from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record


class Helper_Function:
    def Field_Structure(self, field_name, placeholder):
        self.fields[field_name].widget.attrs.update(
            {"class": "form-control", "placeholder": placeholder}
        )
        self.fields[field_name].label = ""


class SignupForms(UserCreationForm, Helper_Function):

    Email = forms.EmailField(
        widget=forms.TextInput(attr={"class": "form-control", "placeholder": "Email"})
    )
    First_Name = forms.EmailField(
        max_length=100,
        widget=forms.TextInput(
            attr={"class": "forms-control", "placeholder": "First_Name"}
        ),
    )
    Last_Name = forms.EmailField(
        max_length=100,
        widget=forms.TextInput(
            attr={"class": "forms-control", "placeholder": "Second_Name"}
        ),
    )

    class meta:
        model = User
        fields = ("username", "firstname", "secondname", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(self, SignupForms).__init__(*args, *kwargs)

        self.Field_Structure("username", "User Name")
        self.Field_Structure("password1", "password")
        self.Field_Structure("password2", "Confirm Password")
        
        self.fields['username'].help_text = (
            '<span class="form-text text-muted">'
            '<small>Required. 150 characters or fewer. Letters, digits, and @/./+/-/_ only.</small></span>'
        )
        self.fields['password1'].help_text = (
            '<ul class="form-text text-muted small">'
            '<li>Your password can\'t be too similar to your other personal information.</li>'
            '<li>Your password must contain at least 8 characters.</li>'
            '<li>Your password can\'t be a commonly used password.</li>'
            '<li>Your password can\'t be entirely numeric.</li>'
            '</ul>'
        )
        self.fields['password2'].help_text = (
            '<span class="form-text text-muted">'
            '<small>Enter the same password as before, for verification.</small></span>'
        )

        
