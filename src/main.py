import pygame
import time
from config import *
from start_menu import StartMenu
from game import Game

# from player import Block

# pygame.display.init()
#
# screen_info = pygame.display.Info()

surface = pygame.display.set_mode(RESOLUTION)

pygame.mixer.init()
pygame.mixer.music.load('sounds/fight_theme.mp3')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)


#---
clock = pygame.time.Clock()
start_menu = StartMenu()
game = Game(surface)

while True:
    for event in pygame.event.get():
        if start_menu.check_events(event):
            game.run_game()
        if event.type == pygame.QUIT:
            exit()
        # elif event.type == pygame.VIDEORESIZE:
        #     print(event.size)
        #     time.sleep(1)
            # if event.w < 800 or event.h < 640:
            #     surface = pygame.display.set_mode(event.size, pygame.RESIZABLE)

    start_menu.draw(surface)
    pygame.display.update()
    clock.tick(FPS)
    pygame.display.set_caption(str(round(clock.get_fps(), 1)))

