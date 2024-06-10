from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from .models import Book, Category, Comment
from .forms import BookCreatForm, CommentForm
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin


class BookListView(generic.ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'
    paginate_by = 12


# class BookDetail(generic.DetailView):
#     model = Book
#     template_name = 'books/book_detail.html'
#     context_object_name = 'book_details'


@login_required(login_url='login')
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    # comments = Comment.objects.filter(book=book)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.book = book
            comment.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = CommentForm()
        comments = book.comments.filter(is_active=True).order_by('-created_at')

    context = {
        'book_details': book,
        'comments': comments,
        'form': form,
    }

    return render(request, 'books/book_detail.html', context)


class BookCreate(LoginRequiredMixin, generic.CreateView):
    form_class = BookCreatForm
    template_name = 'books/add_book.html'
    context_object_name = 'form'

    def form_valid(self, form):  # new
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditBook(LoginRequiredMixin, generic.UpdateView):
    model = Book
    form_class = BookCreatForm
    template_name = 'books/edit_book.html'
    success_url = reverse_lazy('book_list')
    context_object_name = 'form'


class DeleteBook(LoginRequiredMixin, generic.DeleteView):
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
