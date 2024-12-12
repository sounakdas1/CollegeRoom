from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

ROLE_CHOICES = [
    ('student', 'Student'),
    ('teacher', 'Teacher'),
]
COURSES_CHOICES = [
    ('btech','BTech'),
    ('mtech','MTech'),
]

YEAR_CHOICES = [
    ('1st_year', '1st Year'),
    ('2nd_year', '2nd Year'),
    ('3rd_year', '3rd Year'),
    ('4th_year', '4th Year'),
   
]

DPARTMENT_CHOICES = [
    ('CSE','Computer Science Technology'),
    ('IT','Information Technology'),
    ('CT','Ceramic Technology'),
]


class sounakusers(UserCreationForm):
    email = forms.EmailField(max_length=254,required=True,help_text="Required. Enter a valid email address.")
    first_name = forms.CharField(max_length=30, required=True, help_text="Required. Enter your first name.")
    last_name = forms.CharField(max_length=30, required=True, help_text="Required. Enter your last name.")
    password1 = forms.CharField(widget=forms.PasswordInput, label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    

    class Meta:
        model = User
        fields =  ('username', 'first_name', 'last_name', 'email','password1', 'password2')


    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email is in use check twice!')
        
        return email
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("The two password fields didn't match.")

        return cleaned_data