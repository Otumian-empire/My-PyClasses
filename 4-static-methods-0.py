# static methods
# use the staticmethod decorator

class Human:

	@staticmethod
	def speak():
		print("I can speak")
		

Human().speak()

me = Human()
me.speak() # this line will give error
# expected an error.. but there isn't any
# static methods can be called on an instance of a class
# i didn't pass self or any argument to the static method
# there are other cracked gette and setters.. shitty as it may seem
# i don't like it
