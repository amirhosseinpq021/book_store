from django.contrib import admin
from .models import Book, Category, Authors


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'category',)
    search_fields = ('title', 'price', 'category__category_name', 'author__full_name',)
    list_editable = ('price', 'category', 'author',)


admin.site.register(Category)
admin.site.register(Book, BookAdmin)
admin.site.register(Authors)




