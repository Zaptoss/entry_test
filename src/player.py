import pygame
import pygame as pg
from config import RESOLUTION
import random


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.main_states = {
            'stay': pg.transform.scale(pg.image.load('images/neutral_mc.png').convert_alpha(),
                                       (120, 120)).convert_alpha(),
            'flight': pg.transform.scale(pg.image.load('images/flight_mc.png').convert_alpha(),
                                         (120, 120)).convert_alpha()}

        self.image = self.main_states['stay']
        self.rect = self.image.get_rect()

        self.rect.x = 330
        self.rect.y = RESOLUTION[1] - self.image.get_height() - 50

        self.HP = 3
        self.bullets = []
        self.shoot_delay = 0


class Boss(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.HP = 3
        self.boss_states = {
            'stay': pg.transform.scale(pg.image.load('images/neutral_boss.png').convert_alpha(), (200, 305)).convert_alpha(),
            'attack': pg.transform.scale(pg.image.load('images/attack_boss.png').convert_alpha(), (200, 305)).convert_alpha(),
            'death': pg.transform.scale(pg.image.load('images/death_boss.png').convert_alpha(), (200, 305)).convert_alpha()}

        self.image = self.boss_states['stay']
        self.rect = self.image.get_rect()

        self.rect.x = RESOLUTION[0] - self.image.get_width() - 130
        self.rect.y = RESOLUTION[1] - self.image.get_height() - 50

        self.shoot_delay = random.randint(10, 100)
        self.bullets = []

class QuestCharacters(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.main_states = {
            'stay': pg.transform.scale(pg.image.load('images/qc.png').convert_alpha(),
                                       (150, 150)).convert_alpha()}

        self.image = self.main_states['stay']
        self.rect = self.image.get_rect()

        self.rect.x = RESOLUTION[0] - self.image.get_width() - 130
        self.rect.y = RESOLUTION[1] - self.image.get_height() - 50

class Dialog1(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pg.transform.scale(pg.image.load('images/dialog1.png').convert_alpha(), (880, 310)).convert_alpha()
        self.rect = self.image.get_rect()

        self.rect.x = 220
        self.rect.y = 100

class AgreeHelp(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pg.transform.scale(pg.image.load('images/button_help.png').convert_alpha(), (410, 100)).convert_alpha()
        self.rect = self.image.get_rect()

        self.rect.x = 500
        self.rect.y = 400

class RefuseHelp(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pg.transform.scale(pg.image.load('images/button_quit.png').convert_alpha(), (410, 100)).convert_alpha()
        self.rect = self.image.get_rect()

        self.rect.x = 500
        self.rect.y = 500

class Bullet(pygame.sprite.Sprite):

    def __init__(self, speed, x, y):
        super().__init__()
        self.image = pg.transform.scale(pg.image.load('images/bullet.png').convert_alpha(), (90, 30)).convert_alpha()
        self.speed = speed
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
    def update(self):
        self.rect.x += self.speed