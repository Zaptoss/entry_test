import pygame
import pygame as pg
from config import *
from player import Boss, Player, QuestCharacters, Dialog1, AgreeHelp, RefuseHelp, Bullet
import random

clock = pygame.time.Clock()
pygame.mixer.init()
hit_sound = pygame.mixer.Sound('sounds/hit.mp3')
damage_sound = pygame.mixer.Sound('sounds/damage.mp3')
entering_the_room_sound = pygame.mixer.Sound('sounds/entering_the_room.mp3')
entering_the_room_sound.set_volume(0.5)
leaving_the_room_sound = pygame.mixer.Sound('sounds/leaving_the_room.mp3')
leaving_the_room_sound.set_volume(0.5)

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.level = 0
        self.game_surface = pygame.Surface(RESOLUTION).convert_alpha()
        self.game_background_image = pg.image.load('images/coridor.jpg').convert_alpha()
        self.game_background_image = pg.transform.scale(self.game_background_image, RESOLUTION).convert_alpha()
        self.game_surface.blit(self.game_background_image, (0, 0))

        self.game_surface_fight = pygame.Surface(RESOLUTION).convert_alpha()
        self.game_surface_fight_image = pg.transform.scale(pg.image.load('images/fight_room_boss.jpg').convert_alpha(), RESOLUTION).convert_alpha()
        self.game_surface_fight.blit(self.game_surface_fight_image, (0, 0))

        self.game_surface_dead = pygame.Surface(RESOLUTION).convert_alpha()
        self.game_surface_dead_image = pg.transform.scale(pg.image.load('images/death_end.jpg').convert_alpha(),
                                                           RESOLUTION).convert_alpha()
        self.game_surface_dead.blit(self.game_surface_dead_image, (0, 0))

        self.game_surface_happy = pygame.Surface(RESOLUTION).convert_alpha()
        self.game_surface_happy_image = pg.transform.scale(pg.image.load('images/happy_end.jpg').convert_alpha(),
                                                           RESOLUTION).convert_alpha()
        self.game_surface_happy.blit(self.game_surface_happy_image, (0, 0))

        self.boss = Boss()
        self.player = Player()
        self.qc = QuestCharacters()
        self.dialog_sprite = Dialog1()
        self.agree_help = AgreeHelp()
        self.refuse_help = RefuseHelp()

        self.group_sprites_boss = pygame.sprite.Group()
        self.group_sprites_boss.add(self.boss)
        self.group_sprites_boss.add(self.player)

        self.group_sprites_mc = pygame.sprite.Group()
        self.group_sprites_mc.add(self.player)
        self.group_sprites_mc.add(self.qc)
        self.group_sprites_mc.add(self.dialog_sprite)
        self.group_sprites_mc.add(self.agree_help)
        self.group_sprites_mc.add(self.refuse_help)

    def draw(self):
        # self.screen.blit(self.game_surface, (0, 0))
        # self.group_sprites_boss.draw(self.screen)
        if self.level == 0:
            self.screen.blit(self.game_surface, (0, 0))
            self.group_sprites_mc.draw(self.screen)
        elif self.level == 1:
            self.screen.blit(self.game_surface_fight, (0, 0))
            self.group_sprites_boss.draw(self.screen)
            self.group_sprites_boss.update()
        elif self.level == 2:
            self.screen.blit(self.game_surface_happy, (0, 0))
        elif self.level == 3:
            self.screen.blit(self.game_surface_dead, (0, 0))

    def run_game(self):
        jump = 0
        dy = [-(i**2) for i in range(9, 0, -1)] + [i**2 for i in range(1, 10, 1)]
        print(dy)
        print(len(dy))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                    return
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.level == 0:
                        if self.refuse_help.rect.collidepoint(pygame.mouse.get_pos()):
                            exit()
                        elif self.agree_help.rect.collidepoint(pygame.mouse.get_pos()):
                            entering_the_room_sound.play()
                            self.level = 1
                            self.player.rect.x = 100

            keys = pygame.key.get_pressed()

            if self.level == 1:
                if keys[pygame.K_LEFT]:
                    if self.player.rect.x - 14 < 0:
                        self.player.rect.x = 0
                    else:
                        self.player.rect.x -= 14
                if keys[pygame.K_RIGHT]:
                    if self.player.rect.x + 14 > 670:
                        self.player.rect.x = 670
                    else:
                        self.player.rect.x += 14
                if keys[pygame.K_UP] and jump == 0:
                    jump = len(dy)
                if keys[pygame.K_SPACE]:
                    if self.player.shoot_delay == 0:
                        self.player.bullets.append(Bullet(15, self.player.rect.x + self.player.rect.width, self.player.rect.y + self.player.rect.height//2 - 15))
                        self.group_sprites_boss.add(self.player.bullets[-1])
                        self.player.shoot_delay = 20

                if self.player.shoot_delay > 0:
                    self.player.shoot_delay -= 1
                if self.boss.shoot_delay > 0:
                    self.boss.shoot_delay -= 1
                elif self.boss.shoot_delay == 0:
                    self.boss.shoot_delay = random.randint(10, 100)
                    self.boss.bullets.append(Bullet(-15, self.boss.rect.x - 90, self.boss.rect.y + self.boss.rect.height//2 + 30))
                    self.group_sprites_boss.add(self.boss.bullets[-1])

                if jump > 0:
                    self.player.rect.y += dy[-jump]
                    jump -= 1

                for bullet in self.player.bullets:
                    if self.boss.rect.colliderect(bullet.rect):
                        self.group_sprites_boss.remove(bullet)
                        self.player.bullets.remove(bullet)
                        self.boss.HP -= 1
                        hit_sound.play()
                        if self.boss.HP <= 0:
                            self.level = 2
                            leaving_the_room_sound.play()

                for bullet in self.boss.bullets:
                    if self.player.rect.colliderect(bullet.rect):
                        self.group_sprites_boss.remove(bullet)
                        self.boss.bullets.remove(bullet)
                        self.player.HP -= 1
                        damage_sound.play()
                        if self.player.HP <= 0:
                            self.level = 3
                            leaving_the_room_sound.play()

            self.draw()
            pygame.display.update()
            clock.tick(FPS)
            pygame.display.set_caption(str(round(clock.get_fps(), 1)))
