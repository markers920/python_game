
import pygame
from pygame import Color
import sys
from random import random

# pulled some images from
#	http://opengameart.org/

def main():   
	pygame.init()

	game_width = 1200
	game_height = 800
	size = (game_width, game_height)
	
	background = Color(0, 0, 0, 0)

	screen = pygame.display.set_mode(size)

	scale = 0.25
	
	#pull in ufo images
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
	
	#build ufo objects
	ufo_list = []
	number_of_ufo = 10
	for ufo_index in range(number_of_ufo+1):
		rectangle = ufo_images['green'][0].get_rect()
		orig_position = (game_width*random(), game_height*random())
		rectangle = rectangle.move(orig_position)
		speed = [1 + 5*random(), 1 + 5*random()]
		
		ufo_map = {}
		ufo_map['rectangle'] = rectangle
		ufo_map['speed'] = speed
		ufo_map['image_index'] = int(random()*len(ufo_images))
		ufo_map['rotate_speed'] = ((-1)**int(random()*2))
		ufo_list.append(ufo_map)
		print ufo_map
	#END for ufo_index

	#main game loop
	#image_index = 0
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:	#clicking the exit button (red X)
				sys.exit()

			screen.fill(background)
			
			for ufo_index in range(number_of_ufo):
				ufo_list[ufo_index]['rectangle'] = ufo_list[ufo_index]['rectangle'].move(ufo_list[ufo_index]['speed'])
				if ufo_list[ufo_index]['rectangle'].left < 0 or ufo_list[ufo_index]['rectangle'].right > game_width:
					ufo_list[ufo_index]['speed'][0] *= -1
				if ufo_list[ufo_index]['rectangle'].top < 0 or ufo_list[ufo_index]['rectangle'].bottom > game_height:
					ufo_list[ufo_index]['speed'][1] *= -1

				#print ufo_map['image_index']
				im_idx = ufo_list[ufo_index]['image_index']
				
				if im_idx % 8 < 3:
					screen.blit(ufo_images['red'][im_idx], ufo_list[ufo_index]['rectangle'])
				elif im_idx % 8 < 4:
					screen.blit(ufo_images['blue'][im_idx], ufo_list[ufo_index]['rectangle'])
				else:
					screen.blit(ufo_images['green'][im_idx], ufo_list[ufo_index]['rectangle'])
				
				ufo_list[ufo_index]['image_index'] = (im_idx + ufo_list[ufo_index]['rotate_speed']) % number_of_images
			#END for ufo_index in range(number_of_ufo):
			
			pygame.display.flip()
		#END for each event
	#END while True
#END def main():

if __name__ == '__main__':
	main()