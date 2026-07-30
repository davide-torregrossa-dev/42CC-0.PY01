class Plant:
	def __init__(self, name, height, age_in_days):
		self.name = name
		self.height = height
		self.age_in_days = age_in_days
	def show(self):
		str = f"{self.name}: {self.height}cm, {self.age_in_days} days old"
		print(str)

if __name__ == "__main__":
	plants = [
		Plant("Rose", 25, 30),
		Plant("Sunflower", 80, 45),
		Plant("Cactus", 15, 120),
	]
	print("=== Garden Plant Registry ==")
	for plant in plants:
		plant.show()
	
	
