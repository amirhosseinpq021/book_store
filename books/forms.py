from django import forms
from .models import Book, Comment


class BookCreatForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
