
from django.forms import ModelForm
from .models import Bug,Comment
class BugForm(ModelForm):
    class Meta:
        model=Bug
        fields='__all__'
class CommentForm(ModelForm):
    class Meta:
        model=Comment
        fields=['text']
