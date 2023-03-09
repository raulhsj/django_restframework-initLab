from django.urls import path
from books.api.views import BooklistCreateAPIView, BookDetailAPIView, CommentCreateAPIView, CommentDetailAPIView

#
urlpatterns = [
    path('books/', BooklistCreateAPIView.as_view(), name="book-list"),
    path('books/<int:pk>', BookDetailAPIView.as_view(), name="book-detail"),
    path('books/<int:book_id>/addcomment',
         CommentCreateAPIView.as_view(), name="add-comment"),
    path('comment/<int:pk>',
         CommentDetailAPIView.as_view(), name="comment-detail")
]
