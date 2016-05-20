
"""
OLD CODE
"""

class TowerDefenseElemennt(object):
	def __init__(self, speed, direction, image_list, rectangle, orig_position):
		self.speed = speed
		self.direction = direction
		self.images = image_list
		self.rectangle = rectangle
		self.rectangle = self.rectangle.move(orig_position)
	#END def __init__():
	
	def get_speed(self):
		return self.speed
		
	def set_speed(self, speed):
		self.speed = speed
		
	def get_direction(self):
		return self.direction
		
	def set_direction(self, direction):
		self.direction = direction
		
	#TODO; change this
	def get_image(self):
		return self.images[0]
		
	def get_rectangle(self):
		return self.rectangle
	
	def __str__(self):
		return str(self.speed) + ' at ' + str(self.direction) + ' plus image, and rect'
	#END def __str__(self):
	
	def move(self):
		velocity = (self.speed*self.direction[0], self.speed*self.direction[1])
		self.rectangle = self.rectangle.move(velocity)
	#END def move(self):
#END class TowerDefenseElemennt: