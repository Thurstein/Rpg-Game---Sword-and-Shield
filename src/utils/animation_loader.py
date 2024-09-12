from os import walk
import pygame

def import_folder(path):
	surface_list = []

	for _,__,img_files in walk(path): #_,__ means that we don't care about what's being returned here
		for image in img_files:
			full_path = path + '/' + image
			image_surf = pygame.image.load(full_path).convert_alpha()
			surface_list.append(image_surf)

	return surface_list