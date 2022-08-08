from .models import Book
from .serializers import BooksSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# CREATE ........... READ 
@api_view(['GET', 'POST'])
def books_list(request,format=None):
    books = Book.objects.all()

    if(request.method == 'GET'):
        serializer = BooksSerializer(books, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = BooksSerializer(data=request.data)    
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

# UPDATE..............DELETE 
# Get data as per ID
@api_view(['GET', 'PUT', 'DELETE']) 
def update_books(request,id,format=None):
    try: 
        books = Book.objects.get(pk=id)
    except Book.DoesNotExist():
        return Response(status=status.HTTP_404_NOT_FOUND)    
    
    if request.method == 'GET':
        serializer = BooksSerializer(books)
        return Response(serializer.data)

    elif request.method == 'PUT':
            serializer = BooksSerializer(books,data=request.data)    
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':  
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)