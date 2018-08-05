# Write your solutions for 1.5 here!
class Superheros:
	def __init__(self, name, superpower, strength):
		self.name=name
		self.superpower=superpower
		self.strength=strength

	def PrintNameAndStrength(self):
		print("The superhero's name is : " + self.name + " and his strength is: " + self.strength)

	def save_civilian(self,work):
		if self.strength>self.work:
			print(self.strength-self.work)
		else:
			print("Superhero is not strong enough! :(")
			
s=Superheros("Superman","Flying",100)
s.PrintNameAndStrength()
s.save_civilian(70)