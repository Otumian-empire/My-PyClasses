# Cat class
class Cat:

	# constructor
	def __init__(self, name, color):
		self.name = name
		self.color = color

	# cry method
	def cry(self):
		return "Meow! Meow!!"


# sam, an instance of the Cat class
sam = Cat("Sam", "brown");

print(f"Hello, my name is {sam.name}")
print(f"{sam.name}, which is me, is {sam.color}")
print(f"I cry {sam.cry()}")
