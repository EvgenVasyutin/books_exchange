from django.contrib import admin
from .models import Book, Category, Author, Trade, Comment

admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Trade)
admin.site.register(Comment)
