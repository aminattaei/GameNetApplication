from django import forms
from . import models


class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Article_Comment
        fields = '__all__'
