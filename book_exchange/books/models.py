from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'{self.name}'


class Book(models.Model):
    title = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='pictures')
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, null=False, blank=False
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=False, blank=False
    )
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False, blank=False
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self) -> str:
        return f'{self.title}'


class Trade(models.Model):
    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='trade_sender',
    )
    receiver = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='trade_receiver',
    )
    from_book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='from_book_books',
    )
    to_book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='to_book_books',
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.from_book.title} -> {self.to_book.title}'


class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='comment_book',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comment_user',
    )

    def __str__(self) -> str:
        return (
            f'Коментар користувача {self.author.first_name} '
            f'до книги {self.book.title}'
        )
