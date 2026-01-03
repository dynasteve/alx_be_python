class Book:

  def __init__(self, title, author, is_checked_out = False, is_returned = True):
    self.title = title
    self.author = author
    self._is_checked_out = is_checked_out
    self._is_returned = is_returned

  @property
  def is_checked_out(self):
    return self._is_checked_out
  
  @is_checked_out.setter
  def is_checked_out(self, check):
    self._is_checked_out = bool(check)

  @property
  def is_returned(self):
    return self._is_returned
  
  @is_returned.setter
  def is_returned(self, check):
    self._is_returned = bool(check)
  
  def return_book(self, checker):
    self.is_returned = checker

  def check_out_book(self, checker):
    self.is_checked_out = checker


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
        book.check_out_book(True)
        book.return_book(False)
        # print(f"{book.title} by {book.author} has been successfully checked out")

  def return_book(self, title):
    for book in self._books:
      if title == book.title:
        book.check_out_book(False)
        book.return_book(True)
        # print(f"{book.title} by {book.author} has been successfully returned")

  def list_available_books(self):
    if self._books != None or self._books != []:
      for book in self._books:
        if book.is_checked_out == False: print(f"{book.title} by {book.author}")
    else:
      print("The library is empty")
