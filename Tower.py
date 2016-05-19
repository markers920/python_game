
from TowerDefenseElemennt import TowerDefenseElemennt

class Tower(TowerDefenseElemennt):
	def __init__(self, damage, projectile_speed, image_list, rectangle, orig_position):
		self.damage = damage
		self.projectile_speed = projectile_speed
		self.position = orig_position
		TowerDefenseElemennt.__init__(self, 0, [0,0], image_list, rectangle, orig_position)
	#END def __init__(self):
	
	def get_damage(self):
		return self.damage
		
	def get_projectile_speed(self):
		return self.projectile_speed
		
	def get_position(self):
		return self.position
	
	def __str__(self):
		return TowerDefenseElemennt.__str__() + ' damage(' + str(self.damage) + ') projectile_speed(' + self.projectile_speed + ')'
	#END def __str__(self):
#END class Creep: