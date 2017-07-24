class Inventory:

	def __init__(self, size):
		self.weight_limit = size
		self.storage = []

	def isFull(self):
		return len(self.storage) >= self.weight_limit

	def add(self, item, type, amount=1):
		for x in range(amount):
			if(not self.isFull()):
				self.storage.append(item)

	def display(self):
		print("\n---- Inventory ----")
		for x in self.storage:
			print(x)
		print("-------------------\n")
		