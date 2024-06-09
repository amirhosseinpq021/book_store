from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from .models import Book, Category
from .forms import BookCreatForm
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q


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


class EditBook(generic.UpdateView):
    model = Book
    form_class = BookCreatForm
    template_name = 'books/edit_book.html'
    success_url = reverse_lazy('book_list')
    context_object_name = 'form'


class DeleteBook(generic.DeleteView):
    model = Book
    template_name = 'books/delete_book.html'
    success_url = reverse_lazy('book_list')
    context_object_name = 'delete_book'


def search_posts(request):
    keyword = request.GET.get('keyword')

    search_results = Book.objects.filter(
        Q(title__icontains=keyword) | Q(author__full_name__icontains=keyword) | Q(
            category__category_name__icontains=keyword)
    )

    context = {
        'search_results': search_results,
        'keyword': keyword,
    }
    return render(request, 'books/search_result.html', context)


class AllCategory(generic.ListView):
    model = Category
    template_name = 'books/category.html'
    context_object_name = 'category'
