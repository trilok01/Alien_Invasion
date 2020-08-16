import pygame
import sys
def run_game():
	pygame.init()
	screen=pygame.display.set_mode((900, 500))
	bg_color=(230, 230, 230)
	pygame.display.set_caption("Test Program")
	while True:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				sys.exit()
		screen.fill(bg_color)
		pygame.display.flip()
run_game()