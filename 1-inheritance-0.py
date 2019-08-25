# sharing of common functionanlity using classes

# Super (Parent) class
class Animal:
	def __init__(self, name, color, age):
		self.name = name
		self.color = color
		self.age = age

# Sub (Child) class
class Cat(Animal):
	def purr(self):
		print("Purr..!!")

class Dog(Animal):
	def bark(self):
		print("Woof..!!")
		

skull = Cat("Skull Crusher", "red", 5)
skull.purr()

sam = Dog("Sam Ann", "green", 3)
sam.bark()
