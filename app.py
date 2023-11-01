import pygame
import sys
import os

SCREEN_WIDTH = 320
SCREEN_HEIGHT = 640

white = (255, 255, 255)
black = (0, 0, 0)

pygame.init()
pygame.display.set_caption("Simple PyGame Example")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

asset_path = os.getcwd() + "\\asset"
background = pygame.image.load(asset_path + "\\background.png")
background = pygame.transform.smoothscale(background, (1920 , 1080))
background_pos = SCREEN_HEIGHT-1080

bgm = pygame.mixer.Sound(asset_path + "\\bgm.mp3")
bgm.play(-1)

clock = pygame.time.Clock()
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    background_pos += 0.2
    if background_pos >= 0:
        background_pos = 0
    screen.blit(background, (-1100, background_pos))
    pygame.display.update()