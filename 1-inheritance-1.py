# sharing of common functionanlity using classes
# Overriding attributes/methods
# if the parent class has an attributes/methods and the child class implements the same attributes/methods, 
# the parent's implementation is overridden

# Super (Parent) class
class Wolf:
	def __init__(self, name):
		self.name = name
		
	def bark(self):
		print(f" {self.name} Grr.. Woof..!!")
		
# Sub (Child) class
class Dog(Wolf):
	# def bark(self):
	# 	print("Woof.. Woof..!!")
	pass

	
andy = Wolf("Andy Wolf")
andy.bark()

sam = Dog("Sam Dog")
sam.bark()
