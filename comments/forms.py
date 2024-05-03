from django import forms
from comments.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content', 'rating')
        widgets = {
            'content': forms.Textarea(
                attrs={
                    'placeholder': 'Write your comment here...',
                    'class': 'form-control'
                }
            ),
            'rating': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'min': 1,
                    'max': 5,
                    'step': 1,
                    'placeholder': 'Rating (1-5)'
                }
            )
        }
