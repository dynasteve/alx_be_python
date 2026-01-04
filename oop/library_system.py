class Book:
  
  # Initialize the attributes
  def __init__(self, title: str, author: str):
    self.title = title
    self.author = author

  def __str__(self):
    return f"{self.__class__.__name__}: {self.title} by {self.author}"


class EBook(Book):

  def __init__(self, title, author, file_size: int):
    super().__init__(title, author)
    self.file_size = file_size

  def __str__(self):
    return f"{super().__str__()} File Size: {self.file_size}KB"


class PrintBook(Book):
  
  def __init__(self, title, author, page_count: int):
    super().__init__(title, author)
    self.page_count = page_count

  def __str__(self):
    return f"{super().__str__()} Page Count: {self.page_count}"


class Library:
  books = []

  def __init__(self):
    self.books = []

  @classmethod
  def add_book(cls, book):
    cls.books.append(book)

  @classmethod
  def list_books(cls):
    for book in cls.books:
      print(f"{book.__str__()}")