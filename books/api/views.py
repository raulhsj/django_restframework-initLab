from rest_framework.generics import GenericAPIView, CreateAPIView
from books.models import Book, Comment
from books.api.serializers import BookSerializer, CommentSerializer
# from rest_framework.mixin s import ListModelMixin, CreateModelMixin

# Concrete views
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from books.api.permissions import IsAdminOrStaffOrReadOnly, IsCommentOwnerOrReadOnly
from rest_framework.exceptions import ValidationError
from books.api.pagination import SmallPagination, LargePagination


# class BooklistCreateAPIView(ListModelMixin, CreateModelMixin, GenericAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

#     # Listing
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     # Creating
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# ListCreateAPIView has the same behaviour as above
class BooklistCreateAPIView(ListCreateAPIView):
    queryset = Book.objects.order_by('-id')
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrStaffOrReadOnly]
    pagination_class = LargePagination


class BookDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrStaffOrReadOnly]


class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        bookId = self.kwargs.get('book_id')

        checkComments = Comment.objects.filter(
            book_id=bookId, owner=self.request.user)
        if checkComments.exists():
            raise ValidationError(
                'You cannot make more than one comment on a book')
        serializer.save(book_id=bookId, owner=self.request.user)


class CommentDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsCommentOwnerOrReadOnly]
