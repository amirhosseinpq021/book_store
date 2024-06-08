from django.contrib import admin
from .models import Book, Category


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'category')
    search_fields = ('title', 'author', 'price', 'category__category_name')
    list_editable = ('price', 'category',)


admin.site.register(Category)
admin.site.register(Book, BookAdmin)



