 # static_method.py


class MathClass:
 	@staticmethod
 	def add(a,b):#no need to give self
 		return a*b



#we can directly access the func inside the
#class without the object

print(MathClass.add(2,2))