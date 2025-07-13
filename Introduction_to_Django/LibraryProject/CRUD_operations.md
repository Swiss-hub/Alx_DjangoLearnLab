# Create a Book
from bookshelf.models import Book
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()

# Expected Output:
# The book was successfully created and saved.



# Retrieve the Book
from bookshelf.models import Book
book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)

# Expected Output:
# 1984 George Orwell 1949



# Update the Book title
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

# Expected Output:
# Book title successfully updated to Nineteen Eighty-Four




# Delete the Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion
print(Book.objects.all())

# Expected Output:
# <QuerySet []>