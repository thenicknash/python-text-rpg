class MainCharacter():
	"""Builds the main character that the user will control
	"""
	def __init__(self, name, kingdom, lineage, education):
		# Base stats
		self.level = 1
		self.hit_points = 10
		self.strength = 5
		self.stamina = 10
		self.intelligence = 5
		self.heart = 5
		self.luck = 3
		self.charisma = 5
		self.defense = 5
		# Player name, kingdom
		self.name = name
		self.kingdom = kingdom
		# Father's profession (alters stats based upon choice)
		self.lineage = lineage
		# Player education (alters stats based upon choice)
		self.education = education


	def __str__(self):
		print("===================== YOUR JOURNEY BEGINS =====================")
		return "{}, you shall make your motherland of {} proud! Along the way, your father's job being a {} may influence how others view you. Neverthless, with your level of education ({}), you shall surely succeed.".format(self.name, self.kingdom, self.lineage, self.education)
