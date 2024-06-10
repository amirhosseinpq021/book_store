from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookListView.as_view(), name='book_list'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path('book/create/', views.BookCreate.as_view(), name='book_create'),
    path('book/edit/<int:pk>/', views.EditBook.as_view(), name='edit_book'),
    path('book/delete/<int:pk>/', views.DeleteBook.as_view(), name='delete_book'),

    # search box
    path('search/', views.search_posts, name='search_book'),
    # category
    path('category/', views.AllCategory.as_view(), name='category'),
    # edit and delete comments by user
    path('edit/comment/<int:pk>/', views.EditComment.as_view(), name='edit_comments'),
    path('delete/comment/<int:pk>/', views.DeleteComment.as_view(), name='delete_comments'),
]
