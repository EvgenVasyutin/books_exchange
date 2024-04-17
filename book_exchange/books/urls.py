from django.urls import path

from books.views.book import book_create, book_delete, index, book_detail
from books.views.category import categories, category_detail
from books.views.trade import (
    trade_create,
    user_trades,
    trade_delete,
    trade_confirm,
)
from books.views.comment import comment_delete

urlpatterns = [
    path('', view=index, name='index'),
    path('category/', view=categories, name='category'),
    path(
        'category_detail/<int:category_id>',
        view=category_detail,
        name='category_detail',
    ),
    path('create_book/', view=book_create, name='book_create'),
    path('delete_book/<int:book_id>', view=book_delete, name='book_delete'),
    path('book_detail/<int:book_id>', view=book_detail, name='book_detail'),
    path('create_trade/', view=trade_create, name='trade_create'),
    path('my_trades/<int:user_id>', view=user_trades, name='user_trades'),
    path(
        'delete_trade/<int:trade_id>', view=trade_delete, name='trade_delete'
    ),
    path(
        'confirm_trade/<int:trade_id>',
        view=trade_confirm,
        name='trade_confirm',
    ),
    path(
        'delete_comment/<int:comment_id>',
        view=comment_delete,
        name='comment_delete',
    ),
]
