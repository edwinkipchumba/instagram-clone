from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Post, Comment

# class signup form
class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')        
    
    
    # update userform
class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email')

    # update user profile
class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'location', 'profile_picture', 'bio']
    
    
    
    
    
    
    
    
    
    
    # profile form
class ProfileForm(forms.Form):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""  # Removes : as label suffix

    profile_pic = forms.ImageField(required=False)
    username = forms.CharField(max_length=500,required=True)
    first_name = forms.CharField(max_length=500, required=False)
    last_name = forms.CharField(max_length=500, required=False)
    phone_number = forms.CharField(max_length=20, required=False)
    biography = forms.CharField(required=False, widget=forms.Textarea())