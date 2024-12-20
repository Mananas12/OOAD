class Book:
	def __init__(self, title, author, price):
		self.title =title
		self.author = author
		self.price = price

	@property
	def title(self):
		return self.__title

	@title.setter
	def title(self, value: str):
		if not isinstance(value, str):
			raise TypeError("Invalid type")
		if not value:
			raise ValueError("Invalid value")

		self.__title = value

	@property
	def author(self):
		return self.__author

	@author.setter
	def author(self, value: str):
		if not isinstance(value, str):
			raise TypeError("Invalid type")
		if not value:
			raise ValueError("Invalid value")

		self.__author = value

	@property
	def price(self):
		return self.__price

	@price.setter
	def price(self, value: float):
		if not isinstance(value, float):
			raise TypeError("Invalid type")
		if value < 0:
			raise ValueError("Invalid value")

		self.__price = value
		
	def display(self):
		print(f"Title: {self.title}, Author: {self.author}, Price: {self.price}")

book = Book("1984", "George Orwell", 15.99)
book.display()