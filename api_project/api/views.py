from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookSerializer

class BookList(ListAPIView):
    queryset = Book.objects.all()       # Retrieves all books from the database
    serializer_class = BookSerializer   # Uses the serializer to convert data to JSON

# Create your views here.
