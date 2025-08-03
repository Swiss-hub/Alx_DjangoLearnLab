from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):  # Correct import path
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# Create your views here.
