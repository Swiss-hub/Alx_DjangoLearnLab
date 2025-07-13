# Update the Book title
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

# Expected Output:
# Book title successfully updated to Nineteen Eighty-Four
