# data hiding - encapsulation
# this can be achieve by making the attribute or method private
# python doesn't have private keyword so precede 
# the attribute/method identifier with an underscore or a double
# this is more effective if object in import or used as a module
# it isn't that effective
# no underscore = public
# single underscore = protected
# double underscore = private

class Person:

	__name = ''
	__age = 0
	
	def __init__(self, name, age):
		self.__name = name
		self.__age = age
		
me = Person("John Doe", 32)
print(me._Person__name)

