
import pygame
import random

class Creep(pygame.sprite.Sprite):
	SCREENRECT = None
	speed = 13
	animcycle = 1		#animation speed
	image_map = {}
	
	def __init__(self, health):
		pygame.sprite.Sprite.__init__(self, self.containers)
		
		self.health = health
		self.color = self.pick_color()
		
		self.image_index = 0	#int(len(self.images)*random())
		self.image = self.image_map[self.color][self.image_index]
		
		self.rect = self.image.get_rect()
		self.facing = random.choice((-1,1)) * Creep.speed
		self.frame = 0
		if self.facing < 0:
			self.rect.right = Creep.SCREENRECT.right
	#END def __init__(self):
	
	def take_damage(self, damage):
		self.health -= damage
		self.color = self.pick_color()
		if self.health <= 0:
			self.kill()
	#END def take_damage(self, damage):
	
	def pick_color(self):
		if self.health > 30:
			return 'green'
		elif self.health > 10:
			return 'blue'
		else:
			return 'red'
	#END def self.pick_color():

	def update(self):
		self.rect.move_ip(self.facing, 0)
		if not Creep.SCREENRECT.contains(self.rect):
			self.facing = -self.facing;
			self.rect.top = self.rect.bottom + 1
			self.rect = self.rect.clamp(Creep.SCREENRECT)
		self.frame = self.frame + 1
		self.image = self.image_map[self.color][self.frame//self.animcycle%len(self.image_map[self.color])]
	#END def update(self):
#END class Creep: