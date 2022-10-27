import pygame
import pygame as pg
from config import *


class StartMenu:
    def __init__(self):
        self.surface = pygame.Surface(RESOLUTION).convert_alpha()
        self.background_menu = pg.transform.scale(pg.image.load('images/main_menu_pix.png').convert_alpha(), RESOLUTION).convert_alpha()
        self.surface.blit(self.background_menu, (0, 0))
        self.start_button = pygame.Surface(START_BUTTON_SIZE).convert_alpha()
        self.start_button_image = pg.image.load('images/button.png').convert_alpha()
        self.start_button_image = pg.transform.scale(self.start_button_image, START_BUTTON_SIZE).convert_alpha()
        self.start_button_rect = self.surface.blit(self.start_button_image, ((self.surface.get_width()-300)//2,
                                                                             (self.surface.get_height()-170)//2))

    def check_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.start_button_rect.collidepoint(pygame.mouse.get_pos()):
                    return True

    def draw(self, screen: pygame.Surface):
        screen.blit(self.surface, (0, 0))
