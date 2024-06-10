from django.contrib import admin
from .models import Book, Category, Authors, Comment


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'category',)
    search_fields = ('title', 'price', 'category__category_name', 'author__full_name',)
    list_editable = ('price', 'category', 'author',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'user', 'book', 'created_at')
    search_fields = ('text', 'user__username', 'book__title', 'created_at')
    list_editable = ('user', 'book',)


admin.site.register(Category)
admin.site.register(Book, BookAdmin)
admin.site.register(Authors)
admin.site.register(Comment, CommentAdmin)
