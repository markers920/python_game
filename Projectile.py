
from TowerDefenseElemennt import TowerDefenseElemennt

class Projectile(TowerDefenseElemennt):
	def __init__(self, damage, speed, direction, image_list, rectangle, orig_position):
		self.damage = damage
		TowerDefenseElemennt.__init__(self, speed, direction, image_list, rectangle, orig_position)
	#END def __init__(self):
	
	def __str__(self):
		return TowerDefenseElemennt.__str__() + ' damage(' + str(self.damage) + ')'
	#END def __str__(self):
#END class Creep: