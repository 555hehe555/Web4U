from django import forms
from .models import Comments, OwnUserPost


class CommentsForm(forms.ModelForm):
    class Meta():
        model = Comments
        fields = ('name', 'text_comments')


class CreateUserPostForm(forms.ModelForm):
    class Meta():
        model = OwnUserPost
        fields = ['title', 'description', 'img', 'author']
