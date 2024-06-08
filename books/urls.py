from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookListView.as_view(), name='book_list'),
    path('book/<int:pk>/', views.BookDetail.as_view(), name='book_detail'),
    path('book/create/', views.BookCreate.as_view(), name='book_create'),
    path('book/edit/<int:pk>/', views.EditBook.as_view(), name='edit_book'),
    path('book/delete/<int:pk>/', views.DeleteBook.as_view(), name='delete_book'),

]
