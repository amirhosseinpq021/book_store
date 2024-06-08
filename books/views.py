from django.shortcuts import render
from django.views import generic

from .models import Book
from .forms import BookCreatForm


class BookListView(generic.ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'


class BookDetail(generic.DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book_details'


class BookCreate(generic.CreateView):
    form_class = BookCreatForm
    template_name = 'books/add_book.html'
    context_object_name = 'form'
