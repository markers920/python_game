
import pygame
import math

class Projectile(pygame.sprite.Sprite):
	SCREENRECT = None
	speed = 10
	damage = 1	#allow for different kinds, and critsl
	animcycle = 5
	images = []

	def __init__(self, pos, direction):
		pygame.sprite.Sprite.__init__(self, self.containers)
		
		self.frame = 0
		
		#self.image = self.images[0]
		"""if direction[0] > 0 and direction[1] == 0:
			angle = 0
		elif direction[0] < 0 and direction[1] == 0:
			angle = 180
		elif direction[0] == 0 and direction[1] > 0:
			angle = 270
		elif direction[0] == 0 and direction[1] < 0:
			angle = 90
		else:
			angle = math.atan(float(direction[1]) / direction[0]) * (180 / math.pi)
		
		if angle < 0:
			angle += 360
		print direction, angle
		self.image = pygame.transform.rotate(self.images[0], angle)"""
		
		
		if direction[0] == 0 and direction[1] == 0:
			direction[0] = random()
			direction[1] = random()
		
		mag = (direction[0]**2 + direction[1]**2)**0.5
		direction[0] /= mag
		direction[1] /= mag
			
		self.direction = direction
		
		self.angle = math.atan(abs(direction[1] / float(direction[0]))) * (180.0 / math.pi)
		if direction[0] > 0 and direction[1] > 0:		#bottom right
			self.angle = 360 - self.angle
		elif direction[0] > 0 and direction[1] < 0:		#top right
			self.angle = self.angle
		elif direction[0] < 0 and direction[1] > 0:		#bottom left
			self.angle = 180 + self.angle
		elif direction[0] < 0 and direction[1] < 0:		#top left
			self.angle = 180 - self.angle
		#print direction, angle
		
		#90 is the base rotation for htis image
		self.image = self.images[0]
		self.image = pygame.transform.rotate(self.image, 90+self.angle)
		self.rect = self.image.get_rect(midbottom=pos)
	#END def __init__(self, pos):
	
	def get_damage(self):
		return self.damage

	def update(self):
		self.rect.move_ip(self.speed*self.direction[0], self.speed*self.direction[1])
		
		self.frame = self.frame + 1
		self.image = self.images[self.frame//self.animcycle%len(self.images)]
		self.image = pygame.transform.rotate(self.image, 90+self.angle)
		
		#can i do a collision check?
		if self.rect.top <= self.SCREENRECT.top or self.rect.bottom >= self.SCREENRECT.bottom or self.rect.left <= self.SCREENRECT.left or self.rect.right >= self.SCREENRECT.right:
			self.kill()
	#END def update(self):
#END class Creep: