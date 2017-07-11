from django.contrib import admin
from .models import book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'stock')

admin.site.register(book, BookAdmin)

