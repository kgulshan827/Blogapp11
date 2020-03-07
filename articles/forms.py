from .import models
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ('name', 'email', 'body')

class Articleform(forms.ModelForm):
    class Meta:
        model = models.Articles
        fields = ('title', 'slug','body','thumb')