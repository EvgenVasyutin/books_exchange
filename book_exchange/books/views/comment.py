from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponseRedirect
from books.models import Comment
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def comment_delete(
    request: HttpRequest, comment_id: int
) -> HttpResponseRedirect:
    comment = Comment.objects.get(pk=comment_id)
    book = comment.book.id
    if request.user.id == comment.author.id:
        comment.delete()
        messages.success(request, ('Коментар успішно видалено!'))
        return redirect('book_detail', book)
    else:
        messages.error(
            request, ('Ви не можете видалити коментар іншого користувача!')
        )
        return redirect('book_detail', comment.author.id)
