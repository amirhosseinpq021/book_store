from django.contrib import admin
from .models import Book, Category, Authors, Comment


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'category', 'user', 'get_discounted_price',  'book_discount_percentage')
    search_fields = ('title', 'price', 'category__category_name', 'author__full_name', 'user__username',
                     'get_discounted_price', 'book_discount_percentage')
    list_editable = ('price', 'category', 'author', 'user',  'book_discount_percentage')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'discount_percentage_category')
    list_editable = ('discount_percentage_category',)
    search_fields = ('category_name',)
    ordering = ('category_name',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'user', 'book', 'created_at', 'is_active', 'recommend')
    search_fields = ('text', 'user__username', 'book__title', 'created_at', 'is_active', 'recommend')
    list_editable = ('user', 'book', 'is_active', 'recommend')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Authors)
admin.site.register(Comment, CommentAdmin)
