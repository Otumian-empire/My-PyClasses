class Animals:
	def __init__(self, name, age):
		self.name = name
		self.age = age
		print(f"I am {self.name}, an Animal and i am {self.age} years")

	def shout(self):
		return "Animal animal"


Cat = Animals("srappy", 2);
print(Cat.shout())
print(f"Animal name is {Cat.name}")
print(f"Animal age is {Cat.age}")

