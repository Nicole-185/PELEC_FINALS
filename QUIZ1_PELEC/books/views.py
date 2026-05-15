from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Book
from .serializers import BookSerializer


class BookListView(APIView):
    """
    GET  /api/books/  → Return all books
    POST /api/books/  → Add a new book
    """

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(
            {
                "count": books.count(),
                "books": serializer.data,
            },
            status=status.HTTP_200_OK,
        )

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetailView(APIView):
    """
    GET    /api/books/<id>/  → Retrieve a single book
    DELETE /api/books/<id>/  → Delete a book
    """

    def _get_book(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return None

    def get(self, request, pk):
        book = self._get_book(pk)
        if book is None:
            return Response(
                {"error": f"Book with id {pk} not found."},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        book = self._get_book(pk)
        if book is None:
            return Response(
                {"error": f"Book with id {pk} not found."},
                status=status.HTTP_404_NOT_FOUND,
            )
        book_title = book.title
        book.delete()
        return Response(
            {"message": f"Book '{book_title}' deleted successfully."},
            status=status.HTTP_200_OK,
        )