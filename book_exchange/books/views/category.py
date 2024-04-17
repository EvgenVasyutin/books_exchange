from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest
from books.models import Book, Category


def categories(request: HttpRequest) -> HttpResponse:
    all_categories = Category.objects.all()
    context = {'all_categories': all_categories}
    return render(request, 'category/categories.html', context)


def category_detail(request: HttpRequest, category_id: int) -> HttpResponse:
    category = get_object_or_404(Category, pk=category_id)
    category_books = Book.objects.filter(category=category.id)
    context = {'category': category, 'category_books': category_books}
    return render(request, 'category/category_detail.html', context)
