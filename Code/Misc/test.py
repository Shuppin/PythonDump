import json

class Laptop:
	def __init__(self, name, processor, hdd, ram, cost):
		self.name = name
		self.processor = processor
		self.hdd = hdd
		self.ram = ram
		self.cost = cost
		
#create object
laptop1 = Laptop('Dell Alienware', 'Intel Core i7', 512, 8, 2500.00)

#convert to JSON string
jsonStr = json.dumps(laptop1.__dict__)

#print json string
print(laptop1.__dict__)
