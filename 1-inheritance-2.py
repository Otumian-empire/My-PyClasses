# sharing of common functionanlity using classes
# multiple inheritance (indirect inheritance)

# Super (Parent) class
class Wolf:
	def __init__(self, name):
		self.name = name
		
	def bark(self):
		print(f"{self.name} Grr.. Woof..!!")
		
# Sub (Child) class of Wolf
class Dog(Wolf):
	def bark(self):
		print(f"{self.name} Woof.. Woof..!!")
		

# Sub (Child) class of Dog, which makes it inherit from Dog class
# Fox class without bark()
# class Fox(Dog):
# 	pass

# Fox class with bark() it's own implementation
# class Fox(Wolf):
#		def bark(self):
#			print(f"{self.name} Foox.. Woof..!!")

# Fox class with bark() from it's parent class, Dog
# Fox explicitly calls Dog's implementation of bark()
class Fox(Dog):
	def bark(self):
		print(f"{self.name} Foox.. Woof..!!")
		super().bark()


	
andy = Wolf("Andy Wolf")
andy.bark()

sam = Dog("Sam Dog")
sam.bark()

foxy = Fox("Foxy Fox")
foxy.bark()
