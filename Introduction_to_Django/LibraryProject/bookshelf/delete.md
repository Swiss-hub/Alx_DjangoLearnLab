# Delete a Book instance in Django Shell

```python
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion
print(Book.objects.all())

# Expected Output:
# <QuerySet []>