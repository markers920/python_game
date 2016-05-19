
import pygame
from pygame import Color
import sys
from random import random
from time import time

#from TowerDefenseClasses import *

from TowerDefenseElemennt import TowerDefenseElemennt
from Creep import Creep
from Tower import Tower
from Projectile import Projectile

# pulled some images from
#	http://opengameart.org/



def get_images():
	#pull in ufo images
	scale = 0.25
	ufo_images = {}
	ufo_images['red'] = []
	ufo_images['green'] = []
	ufo_images['blue'] = []
	number_of_images = 25
	for index in range(number_of_images):
		index_str = str(index).zfill(4)
		
		ufo = pygame.image.load('ufo_red/red_ufo_gmc_' + index_str + '.png')
		ufo_w, ufo_h = ufo.get_size()
		ufo = pygame.transform.scale(ufo, (int(ufo_w*scale), int(ufo_h*scale)))
		ufo_images['red'].append(ufo)
		
		ufo = pygame.image.load('ufo_green/green_ufo_gmc_' + index_str + '.png')
		ufo_w, ufo_h = ufo.get_size()
		ufo = pygame.transform.scale(ufo, (int(ufo_w*scale), int(ufo_h*scale)))
		ufo_images['green'].append(ufo)
		
		ufo = pygame.image.load('ufo_blue/blue_ufo_gmc_' + index_str + '.png')
		ufo_w, ufo_h = ufo.get_size()
		ufo = pygame.transform.scale(ufo, (int(ufo_w*scale), int(ufo_h*scale)))
		ufo_images['blue'].append(ufo)
	#END for index
	return (number_of_images, ufo_images)
#END def get_images():


def build_objects(number_of_ufo, ufo_images, game_width, game_height):
	#build ufo objects
	creep_list = []
	for ufo_index in range(number_of_ufo+1):
		health = 100
		
		speed = 5
		
		direction = [1 + 10*random(), 1 + 10*random()]
		mag = (direction[0]**2 + direction[1]**2)**0.5
		direction[0] *= (((-1)**int(2.0*random())) / mag)
		direction[1] *= (((-1)**int(2.0*random())) / mag)
		
		image_list = ufo_images['green']
		
		rectangle = ufo_images['green'][0].get_rect()
		
		orig_position = (0.1*game_width + 0.8*game_width*random(), 0.1* game_height + 0.8*game_height*random())
		
		creep_list.append(Creep(health, speed, direction, image_list, rectangle, orig_position))
		#print ufo_map
	#END for ufo_index
	
	return creep_list
#END def build_objects():


def main():   
	pygame.init()

	game_width = 1200
	game_height = 800
	size = (game_width, game_height)
	
	background = Color(0, 0, 0, 0)

	screen = pygame.display.set_mode(size)

	(number_of_images, ufo_images) = get_images()
	
	number_of_creeps = 10
	creep_list = build_objects(number_of_creeps, ufo_images, game_width, game_height)
	
	#TOWER
	tower_image = pygame.image.load('tower/niXoRookT.png')
	tower_w, tower_h = tower_image.get_size()
	tower_scale = 0.10
	tower_image = pygame.transform.scale(tower_image, (int(tower_w*tower_scale), int(tower_h*tower_scale)))
	tower_rectangle = tower_image.get_rect()
	
	#PROJECTILE
	projectile_image = pygame.image.load('throwable/bomb.png')
	projectile_w, projectile_h = projectile_image.get_size()
	projectile_scale = 0.1
	projectile_image = pygame.transform.scale(projectile_image, (int(projectile_w*projectile_scale), int(projectile_h*projectile_scale)))
	projectile_rectangle = projectile_image.get_rect()
	

	#main game loop
	tower_list = []
	projectile_list = []
	last_shot_time = 0
	while True:
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:	#clicking the exit button (red X)
				sys.exit()
			
			if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed() == (0,0,1):
				tower_list.append(Tower(1000, 15, [tower_image], tower_rectangle, pygame.mouse.get_pos()))
				#print event, pygame.mouse.get_pressed(), pygame.mouse.get_pos()
		#END for each event
			

		screen.fill(background)
		
		for creep in creep_list:
			creep.move()
			old_direction = creep.get_direction()
			if creep.get_rectangle().left < 0 or creep.get_rectangle().right > game_width:
				creep.set_direction([-1 * old_direction[0], old_direction[1]])
			if creep.get_rectangle().top < 0 or creep.get_rectangle().bottom > game_height:
				creep.set_direction([old_direction[0], -1 * old_direction[1]])

			#TODO: blit seems slow... work around?
			screen.blit(creep.get_image(), creep.get_rectangle())
		#END for creep_index in range(number_of_ufo):
		
		shoot_out = False
		if time() - last_shot_time > 0.5:
			shoot_out = True
			last_shot_time = time()
			
		for tower in tower_list:
			screen.blit(tower.get_image(), tower.get_rectangle())
			if shoot_out:
				tower_position = tower.get_position()
				mouse_position = pygame.mouse.get_pos()
				direction = [mouse_position[0] - tower_position[0], mouse_position[1] - tower_position[1]]
				mag = (direction[0]**2 + direction[1]**2)**0.5
				if mag > 0:
					direction[0] /= mag
					direction[1] /= mag
					projectile_list.append(Projectile(tower.get_damage(), tower.get_projectile_speed(), direction, [projectile_image], projectile_rectangle, tower_position))
		#ENDfor tower in tower_list:
		
		remove_projectiles = []
		for projectile in projectile_list:
			projectile.move()
			screen.blit(projectile.get_image(), projectile.get_rectangle())
			
			if projectile.get_rectangle().left < 0 or projectile.get_rectangle().right > game_width or projectile.get_rectangle().top < 0 or projectile.get_rectangle().bottom > game_height:
				remove_projectiles.append(projectile)
		#END for projectile in projectile_list:
		
		for p in remove_projectiles:
			projectile_list.remove(p)
		#END for p in remove_projectiles:
		
		pygame.display.flip()
		
	#END while True
#END def main():

if __name__ == '__main__':
	main()