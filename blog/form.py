from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Comments, OwnUserPost

from rest_api.models import CustomUser


class CommentsForm(forms.ModelForm):
    class Meta():
        model = Comments
        fields = ['text_comments']


class CreateUserPostForm(forms.ModelForm):
    class Meta():
        model = OwnUserPost
        fields = ['title', 'description', 'img']


class CreateUserForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'email']