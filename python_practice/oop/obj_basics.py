#obj_basics.py


class Laptop:

	#common for all the obj that is created
	processor = "intel"

	def __init__(self):
		self.device = "Laptop"
		self.power_supply = "Battery"
		self.price_range = [1000,2000]

	def brand(self,brandname):
		self.brandname = brandname


	def price(self,price):
		self.price = price


lap1 = Laptop()

print(lap1.processor)

print(lap1.device)
print(lap1.power_supply)
print(lap1.price_range)

lap1.brand("Lenova")

print(lap1.brandname)

lap1.price(1500)