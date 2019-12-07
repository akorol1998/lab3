from PyQt5 import QtCore, QtGui, QtWidgets, uic
import datetime
import numpy as np
import sys


NAMES = ["Artem", "VLad", "Oleksandr", "Julyyy", "Kate", "Alina"]
SURNAMES = ["Stenvy", "Karp", "Fedorich", "Carpenter", "Moris", "Schevchenko"]

# Task 1

class A(QtWidgets.QMainWindow):

	def __init__(self):
		super(A, self).__init__()
		uic.loadUi("ui_files/window_1.ui", self)
		self.pushButton_3.clicked.connect(self.postAdd)
		self.pushButton_2.clicked.connect(self.multiEqual)
		self.pushButton_1.clicked.connect(self.decrement)


	def decrement(self):
		print(self.spinBox_2.value() - self.spinBox_1.value())
		self.label_3.setText(str(self.spinBox_2.value() - self.spinBox_1.value()))

	def multiEqual(self):
		self.label_3.setText(str(self.spinBox_1.value() * self.spinBox_2.value()))
		try:
			self.spinBox_2.setValue(self.spinBox_1.value() * self.spinBox_2.value())
		except OverflowError:
			pass

	def postAdd(self):
		self.label_3.setText(str(self.spinBox_1.value() + self.spinBox_2.value() + 1))


# Task 2

class B(A):
	def __init__(self):
		super(B, self).__init__()
		uic.loadUi("ui_files/task_2.ui", self)
		self.pushButton_6.clicked.connect(self.evaluate)
		self.button_list = [self.spinBox_3,
							self.spinBox_4,
							self.spinBox_6]

	def evaluate(self):
		i = 0
		res = 0
		while i < len(self.button_list):
			res += self.button_list[i].value()
			i -= -1
		self.label_9.setText(str(res))


# Task 3

class Student():
	def __init__(self, name, surname, num: int, data: datetime):
		self.__surname = surname
		self.__name = name
		self.__number = num
		self.__date = data
	
	@property
	def number(self):
		return self.__number
	
	@property
	def name(self):
		return self.__name
	
	def __str__(self):
		return f"Surname: {self.__surname}, Name: {self.__name}, Number: {self.__number}, Date: {self.__date}"


class Group():
	def __init__(self):
		self.arr: Student = []
		self.generate_students()
	
	def generate_students(self):
		for i in range(6):
			stud = Student(NAMES[np.random.randint(0,6)], SURNAMES[np.random.randint(0,6)], i, datetime.datetime.now())
			self.arr.append(stud)
	
	def get_student_by_number(self, num: int) -> Student:
		for i in self.arr:
			if i.number == num:
				return i
		print("No student with such a number found")
		return None
	
	def get_student_by_index(self, index: int) -> Student:
		for i in range(len(self.arr)):
			if i == index:
				return self.arr[i]
		print("No student under such index")
		return None

	def get_student_by_name(self):
		name = input("Enter Studnet`s name: ")
		for i in self.arr:
			if i.name == name:
				print("Information:", i)
				return 
		print("No student with such a name")

if __name__ == "__main__":
	
	# app = QtWidgets.QApplication(sys.argv)
	# # Task 1
	# window = A()
	# # Task 2
	# window = B()
	# window.show()
	# sys.exit(app.exec_())

	# Task 3
	# g = Group()
	# print(g.get_student_by_number(1))
	# print(g.get_student_by_number(2))

	# print(g.get_student_by_index(3))
	# print(g.get_student_by_index(4))

	# g.get_student_by_name()

	
