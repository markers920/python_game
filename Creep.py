
from TowerDefenseElemennt import TowerDefenseElemennt

class Creep(TowerDefenseElemennt):
	def __init__(self, health, speed, direction, image_list, rectangle, orig_position):
		self.health = health
		TowerDefenseElemennt.__init__(self, speed, direction, image_list, rectangle, orig_position)
	#END def __init__(self):
	
	def __str__(self):
		return TowerDefenseElemennt.__str__() + ' health(' + str(self.health) + ')'
	#END def __str__(self):
#END class Creep: