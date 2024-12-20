class Student:
	def __init__(self, name: str, marks = []):
		self.name = name
		self.marks = marks

	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self, value: str):
		if not isinstance(value, str):
			raise TypeError("Invalid type")
		if not value:
			raise ValueError("Invalid value")

		self.__name = value

	def add_mark(self, grade: int):
		if not isinstance(grade, int):
			raise TypeError("Invalid type")
		if grade < 0:
			raise ValueError("Invalid value")
		elif grade > 100:
			raise ValueError("Invalid value")
		else:
			self.marks.append(grade)

	def average(self):
		return sum(self.marks) / len(self.marks)

student = Student("Aram", [])
student.add_mark(80)
student.add_mark(90)
print(student.average())