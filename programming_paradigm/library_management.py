class Book:

  def __init__(self, title, author, is_checked_out = False):
    self.title = title
    self.author = author
    self._is_checked_out = is_checked_out

  @property
  def is_checked_out(self):
    return self._is_checked_out
  
  @is_checked_out.setter
  def is_checked_out(self, check):
    self._is_checked_out = bool(check)
  


class Library:

  def __init__(self):
    self._books = []
    pass

  def add_book(self, book):
    self._books.append(book)
    pass

  def check_out_book(self, title):
    # First check if book title is among the list of books
    for book in self._books:
      if title == book.title:
        # Set the book to be checked out
        book.is_checked_out = True
        # print(f"{book.title} by {book.author} has been successfully checked out")

  def return_book(self, title):
    for book in self._books:
      if title == book.title:
        book.is_checked_out = False
        # print(f"{book.title} by {book.author} has been successfully returned")

  def list_available_books(self):
    if self._books != None or self._books != []:
      for book in self._books:
        if book.is_checked_out == False: print(f"{book.title} by {book.author}")
    else:
      print("The library is empty")
