from django import forms
from .models import Book, Comment


class BookCreatForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'cover', 'author', 'description', 'price', 'category')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text', 'recommend',)
