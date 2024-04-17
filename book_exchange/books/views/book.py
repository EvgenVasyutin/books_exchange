from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from books.models import Book
from books.forms import BookForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from books.forms import CommentForm


def index(request: HttpRequest) -> HttpResponse:
    all_books = Book.objects.all()
    paginator = Paginator(all_books, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'index.html', context)


@login_required(login_url='login')
def book_detail(request: HttpRequest, book_id: int) -> HttpResponse:
    book = Book.objects.get(pk=book_id)
    comment_form = CommentForm(request.POST or None)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.author = request.user
        comment.book = book
        comment.save()
        return redirect('book_detail', book_id)
    else:
        comment_form = CommentForm()
    context = {'comment_form': comment_form, 'book': book}
    return render(request, 'book/book_detail.html', context)


@login_required(login_url='login')
def book_create(request: HttpRequest) -> HttpResponse | HttpResponseRedirect:
    book_form = BookForm(request.POST, request.FILES)
    if request.method == 'POST':
        if book_form.is_valid():
            book = book_form.save(commit=False)
            book.owner = request.user
            book.save()
            messages.success(
                request,
                ('Ви успішно створили книгу на обмін!'),
            )
            return redirect('profile', request.user.id)
    else:
        book_form = BookForm()
    context = {'book_form': book_form}
    return render(request, 'book/book_create.html', context)


@login_required(login_url='login')
def book_delete(request: HttpRequest, book_id: int) -> HttpResponseRedirect:
    book = Book.objects.get(pk=book_id)
    if request.user.id == book.owner.id:
        book.delete()
        messages.success(request, ('Книга успішно видалена!'))
        return redirect('profile', request.user.id)
    else:
        messages.error(
            request, ('Ви не можете видалити книгу іншого користувача!')
        )
        return redirect('profile', request.user.id)
