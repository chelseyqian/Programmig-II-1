
class Class1:
	def __init__(self, num):
		self.n = num
		self.cost = 0
		
	def calc(self):
		self.cost += 1.75 + 0.05 * self.n * self.n
		
	def getCost(self):
		return self.cost
