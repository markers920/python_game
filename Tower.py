
import pygame

class Tower(pygame.sprite.Sprite):
	SCREENRECT = None
	speed = 10
	bounce = 24
	gun_offset = -11
	images = []
	
	def __init__(self):
		pygame.sprite.Sprite.__init__(self, self.containers)
		self.image = self.images[0]
		self.rect = self.image.get_rect().move(pygame.mouse.get_pos())
		#self.reloading = 0
		#self.origtop = self.rect.top
		#self.facing = -1
	#END def __init__(self):

	"""def move(self, direction):
		if direction: 
			self.facing = direction
		self.rect.move_ip(direction*self.speed, 0)
		self.rect = self.rect.clamp(SCREENRECT)
		if direction < 0:
			self.image = self.images[0]
		elif direction > 0:
			self.image = self.images[1]
		self.rect.top = self.origtop - (self.rect.left//self.bounce%2)
	#END def move(self, direction):"""

	def center_position(self):
		return (self.rect.centerx, self.rect.centery)
	#END def gunpos(self):
#END class Creep: