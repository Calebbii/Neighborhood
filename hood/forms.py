from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Post, Business, Neighborhood

class SignUpForm(UserCreationForm):
  first_name = forms.CharField(max_length=100, help_text='Last Name')
  last_name = forms.CharField(max_length=100, help_text='Last Name')
  email = forms.EmailField(max_length=150, help_text='Email')

  class Meta:
    model = User
    fields = ('username', 'email', 'password1', 'password2')

class CreateNeighborHoodForm(forms.ModelForm):
  class Meta:
    model = Neighborhood
    fields = ['name','location','neighborhood_logo','description','population','police_contact','hospital_contact']

class CreateBusinessForm(forms.ModelForm):
  class Meta:
    model = Business
    fields = ('name','description','image','email')

class CreatePostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ('title','post','image')

class UpdateBusinessForm(forms.ModelForm):
  class Meta:
    model = Business
    fields = ['name','description','image','email']

class UpdatePostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ['title','post','image']

class UpdateProfileFrom(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ['first_name','last_name','bio','profile_picture','location']

class UpdateUser(forms.ModelForm):
  email = forms.EmailField()
  class Meta:
    model = User
    fields = ['username','email']

class UpdateNeighborhoodForm(forms.ModelForm):
  class Meta:
    model = Neighborhood
    fields = ['name','location','neighborhood_logo','description','population','police_contact','hospital_contact']