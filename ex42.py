class Animal(object):
	pass
	
# Dog is-a class of Animal.
class Dog(Animal):
	
	
	def __init__(self, name):
		# "name" is a Dog.
		self.name = name
		
# Cat is-a class of Animal.
class Cat(Animal):
	
	def __init__(self, name):
		# "name" is a Cat.
		self.name = name
		
# Person is a class containing (has-a) "objects"(people)
class Person(object)
	
	def __init__(self, name):
		# "name" is a person.
		self.name = name
		
		# Person has-a pet of some kind.
		self.pet = none
		
# Employee is a class containing (has-a) Person.
class Employee(Person)

	def __init__(self, name, salary):
		# Employee is a 
		super(Employee, self).__init__(name)
		#Employee has-a salary
		self.salary = salary
	
# Fish has-a object	
class Fish(object)
	pass
	
# Salmon is-a Fish
class Salmon(Fish)
	pass
	
# Halibut is-a Fish
class Halibut(Fish)
	pass
	
# rover is-a Dog
rover = Dog("Rover")

# satan is-a Cat
satan = Cat("Satan")

# Mary is a person
mary = Person("Mary")

# Mary has-a pet
mary.pet = satan

# Frank is-a employee and has-a salary
frank = Employee("Frank", 120000)

# Frank has-a pet
frank.pet = rover

# Flipper is-a fish
flipper = Fish()

# Crouse is-a Salmon
crouse = Salmon()

# Harry is-a Halibut
harry = Halibut()
