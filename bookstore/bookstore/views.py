from .models import Book
from .serializers import BooksSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def books_list(request,format=None):
    books = Book.objects.all()
    serializer = BooksSerializer(books, many=True)
    return Response(serializer.data)

