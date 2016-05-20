
#inspiration from the pygame aliens example
# http://66.media.tumblr.com/2a29a324317a09f9744886bb70f5c124/tumblr_nbq2z80NAq1s5xy3ro1_1280.gif
# http://animizer.net/en/gif-apng-splitter

import random
import os.path
import os
import time

import pygame
from pygame.locals import *

from Explosion import Explosion
from Creep import Creep
from Tower import Tower
from Projectile import Projectile


###############################################################################

SCREENRECT     = Rect(0, 0, 1530, 960)

#main_dir = os.path.split(os.path.abspath(__file__))[0]
main_dir = '.'

###############################################################################

def load_image(file, scale=1.0, transparent_color=None):
	#loads an image, prepares it for play
	
	#try:
	surface = pygame.image.load(file)
	
	surface_w, surface_h = surface.get_size()
	surface = pygame.transform.scale(surface, (int(surface_w*scale), int(surface_h*scale)))
	
	if transparent_color != None:
		surface.set_colorkey( transparent_color, RLEACCEL )
		
	#except pygame.error:
	#	raise SystemExit('Could not load image "%s" %s'%(file, pygame.get_error()))
	return surface
#END def load_image(file):

def load_images(path_list, scale=1.0, transparent_color=None):
	imgs = []
	
	dir = main_dir
	for p in path_list:
		dir = os.path.join(dir, p)
		
	for file in os.listdir(dir):
		full_path = os.path.join(dir, file)
		imgs.append(load_image(full_path, scale, transparent_color))
	return imgs
#END def load_images(*files):

###############################################################################

def main():
	# Initialize pygame
	pygame.init()
	
	clock = pygame.time.Clock()
	
	
	# Set the display mode
	winstyle = 0  # |FULLSCREEN
	bestdepth = pygame.display.mode_ok(SCREENRECT.size, winstyle, 32)
	screen = pygame.display.set_mode(SCREENRECT.size, winstyle, bestdepth)
	
	
	#Set the SCREENRECT in the classes
	Creep.SCREENRECT = SCREENRECT
	Tower.SCREENRECT = SCREENRECT
	Projectile.SCREENRECT = SCREENRECT
	
	
	#decorate the game window
	#icon = pygame.transform.scale(Creep.images[0], (32, 32))
	#pygame.display.set_icon(icon)							#Change the system image for the display window
	pygame.display.set_caption('Markers Tower Defense')		#window name
	#pygame.mouse.set_visible(0)	#TODO: set cursor as a target
	
	
	#create the background, tile the bgd image
	bgdtile = load_image(os.path.join('backgrounds', 'background.jpg'))
	background = pygame.Surface(SCREENRECT.size)
	for x in range(0, SCREENRECT.width, bgdtile.get_width()):
		for y in range(0, SCREENRECT.height, bgdtile.get_height()):
			background.blit(bgdtile, (x, y))
	screen.blit(background, (0,0))
	pygame.display.flip()
	
	
	#set the Tower images
	img = load_image(os.path.join('tower', 'tower.png'), 0.2)
	Tower.images = [img]
	
	#set the Creep images
	Creep.image_map = {}
	for color in ['red', 'green', 'blue']:
		Creep.image_map[color] = load_images(['ufo_' + color], 0.20)
		
	#set the explosion images
	Explosion.images = load_images(['throwable', 'explosion_all'], 5.0)
	
	#set the Projectile images
	Projectile.images = load_images(['throwable', 'fireball'], 0.3, (0,0,255))
	
	

	# Initialize Game Groups
	creeps = pygame.sprite.Group()
	projectiles = pygame.sprite.Group()
	towers = pygame.sprite.Group()
	explosions = pygame.sprite.Group()
	all = pygame.sprite.RenderUpdates()
	
	#assign default groups to each sprite class
	Creep.containers = creeps, all
	Projectile.containers = projectiles, all
	Tower.containers = towers, all
	Explosion.containers = explosions, all
	
	
	tower_cycle = 5
	tower_load = tower_cycle
	
	creep_cycle = 25
	creep_load = creep_cycle
	
	projectile_cycle = 10
	projectile_load = projectile_cycle
	
	score = 0
	
	while True:	#player.alive():
		loop_start_time = time.time()
		
		#get input
		for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
				return
		#END for event
		
		#key and mouse state
		keystate = pygame.key.get_pressed()
		mousestate = pygame.mouse.get_pressed()
		mouse_position = pygame.mouse.get_pos()
		
		# clear/erase the last drawn sprites
		all.clear(screen, background)
		
		#update all the sprites
		all.update()
		
		
		#load new creeps
		creep_load -= 1
		if creep_load < 0:
			#Creep(int(random.random()*10))
			Creep(40)
			creep_load = creep_cycle
			
		#load new projectiles
		projectile_load -= 1
		if projectile_load < 0:
			for t in towers:
				tower_position = t.center_position()
				projectile_direction = [mouse_position[0] - tower_position[0], mouse_position[1] - tower_position[1]]
				Projectile(t.center_position(), projectile_direction)
			projectile_load = projectile_cycle
			
		
		#load new towers
		tower_load -= 1
		if mousestate == (0,0,1) and tower_load < 0:
			Tower()
			tower_load = tower_cycle
		
		#detect collisions
		"""for p in projectiles:
			aliens_hit = pygame.sprite.spritecollide(p, creeps, False)
			if len(aliens_hit) > 0:
				p.kill()
				for a in aliens_hit:
					Explosion(a)
					a.take_damage(p.get_damage())"""
					
		for c in creeps:
			for p in pygame.sprite.spritecollide(c, projectiles, False):
				p.kill()
				Explosion(c)
				c.take_damage(p.get_damage())
					
		
		
		#draw the scene
		dirty = all.draw(screen)
		pygame.display.update(dirty)

		loop_end_time = time.time()
		#print loop_end_time - loop_start_time
		
		#cap the framerate
		clock.tick(30)
		
	#END while player.alive():
	
	pygame.time.wait(1000)
	pygame.quit()
	
#END def main():



if __name__ == '__main__':
	main()