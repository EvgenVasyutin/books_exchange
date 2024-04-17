from django import forms
from django.db.models import QuerySet
from books.models import Book, Comment, Trade
import typing as t


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        exclude = ('owner',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {'text': 'Залишити відгук'}


class TradeForm(forms.ModelForm):
    def __init__(self, *args: t.Any, **kwargs: t.Any) -> QuerySet:
        user = kwargs.pop('user', None)
        super(TradeForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['to_book'].queryset = Book.objects.filter(owner=user)
            self.fields['from_book'].queryset = Book.objects.exclude(
                owner=user
            )

    class Meta:
        model = Trade
        fields = ('from_book', 'to_book')
        labels = {
            'to_book': 'Книга, яку ви пропонуєте',
            'from_book': 'Книга, яку ви хочете отримати',
        }
