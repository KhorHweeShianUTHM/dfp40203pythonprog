class Book:
	def __init__(self,book_title,author):
		self.book_title = book_title
		self.author = author

book1 = Book("Science","Carl Sagan")
print(book1.book_title,book1.author)
