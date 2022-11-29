from .models import Comment
from django.forms import ModelForm, TextInput, Textarea


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["title", "comment"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter ur name'
            }),
            "comment": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write ur comment here'
            }),
        }