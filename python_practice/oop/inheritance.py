#inheritance.py



class Pet:

	def __init__(self,name,age):
		self.name = name
		self.age = age

	def show(self):
		print(f"I am {self.name} and i am {self.age} yr old")
	
	def speak(self):
		print(f"I dont know")

#from pet
class Cat(Pet):

	def __init__(self,name,age,color):
		self.color = color

		#super class
		super().__init__(name,age) #calling the init from super class


	def speak(self):
		print("I am cat")

#from pet
class Dog(Pet):
	def speak(self):
		print("I am Dog")

p = Pet("Tom",13)
p.speak()

#here we give the argument even though we 
#dont have the init in Cat Class,
# this will initialize the init in Parent class

c = Cat("Sam",19,"Black")
c.speak()

d = Dog("ram",11)
d.speak()