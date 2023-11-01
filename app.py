import pygame
import os

from modules.Bullet import Bullet
from modules.Enemy import Enemy

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

posx = SCREEN_WIDTH // 2
posy = SCREEN_HEIGHT - 100
rad = 20
playerColor = (102, 255, 102)
hp = 5
speed = 3

playerBulletColor = (102, 255, 102)
playerBulletList = []

enemyList = []
enemyBulletList = []

FLAG_DOWN = False
FLAG_UP = False
FLAG_RIGHT = False
FLAG_LEFT = False
FLAG_SHOOT = False

frame_tick = 0
clock = pygame.time.Clock()

running = True
while running:
    clock.tick(60)
    frame_tick += 1
    screen.blit(background, (-1100, background_pos))
    background_pos += 0.2
    if background_pos >= 0:
        background_pos = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                FLAG_DOWN = True
            if event.key == pygame.K_UP:
                FLAG_UP = True
            if event.key == pygame.K_RIGHT:
                FLAG_RIGHT = True
            if event.key == pygame.K_LEFT:
                FLAG_LEFT = True
            if event.key == pygame.K_SPACE:
                FLAG_SHOOT = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                FLAG_DOWN = False
            if event.key == pygame.K_UP:
                FLAG_UP = False
            if event.key == pygame.K_RIGHT:
                FLAG_RIGHT = False
            if event.key == pygame.K_LEFT:
                FLAG_LEFT = False
            if event.key == pygame.K_SPACE:
                FLAG_SHOOT = False
    
    if FLAG_DOWN == True:
        posy += speed
    if FLAG_UP == True:
        posy -= speed
    if FLAG_RIGHT == True:
        posx += speed
    if FLAG_LEFT == True:
        posx -= speed

    if FLAG_SHOOT == True:
        playerBulletList.append(Bullet(posx-10, posy - rad, playerBulletColor, 0, -9))
        playerBulletList.append(Bullet(posx, posy - rad, playerBulletColor, 0, -9))
        playerBulletList.append(Bullet(posx+10, posy - rad, playerBulletColor, 0, -9))

    for bullet in playerBulletList:
        pygame.draw.circle(screen, bullet.color, (bullet.x, bullet.y), bullet.rad)
        bullet.update()

    for bullet in playerBulletList:
        flag = False
        if bullet.x < 0 or bullet.x > SCREEN_WIDTH:
            flag = True
        if bullet.y < 0 or bullet.y > SCREEN_HEIGHT:
            flag = True
        if flag == True:
            playerBulletList.remove(bullet)
    
    # 잡몹 등장패턴
    if frame_tick == 120:
        enemyList.append(Enemy(0, 50, (255, 80, 0), 2, 0))
    if frame_tick == 140:
        enemyList.append(Enemy(0, 50, (255, 80, 0), 2, 0))
    if frame_tick == 160:
        enemyList.append(Enemy(0, 50, (255, 80, 0), 2, 0))
    if frame_tick == 200:
        for enemy in enemyList:
            enemyBulletList.append(Bullet(enemy.x, enemy.y, (255, 80, 0), (posx-enemy.x)/80, (posy-enemy.y)/80))
    if frame_tick == 300:
        enemyList.append(Enemy(SCREEN_WIDTH,50,(255,80,0),-2,0))
    if frame_tick == 320:
        enemyList.append(Enemy(SCREEN_WIDTH,50,(255,80,0),-2,0))
    if frame_tick == 340:
        enemyList.append(Enemy(SCREEN_WIDTH,50,(255,80,0),-2,0))
    if frame_tick == 380:
        for enemy in enemyList:
            enemyBulletList.append(Bullet(enemy.x, enemy.y, (255, 80, 0), (posx-enemy.x)/80, (posy-enemy.y)/80))

    # 잡몹 draw
    for enemy in enemyList:
        pygame.draw.circle(screen, enemy.color, (enemy.x, enemy.y), enemy.rad)
        enemy.update_pattern1()
    
    for bullet in enemyBulletList:
        pygame.draw.circle(screen, bullet.color, (bullet.x, bullet.y), bullet.rad)
        bullet.update()

    for bullet in enemyBulletList:
        flag = False
        if bullet.x < 0 or bullet.x > SCREEN_WIDTH:
            flag = True
        if bullet.y < 0 or bullet.y > SCREEN_HEIGHT:
            flag = True
        if flag == True:
            enemyBulletList.remove(bullet)
    

    for enemy in enemyList:
        flag = False
        if enemy.x < 0 or enemy.x > SCREEN_WIDTH:
            flag = True
        if enemy.y < 0 or enemy.y > SCREEN_HEIGHT:
            flag = True
        if flag == True:
            enemyList.remove(enemy)

    for enemy in enemyList:
        for bullet in playerBulletList:
            if ((enemy.x - bullet.x)**2 + (enemy.y - bullet.y)**2)**0.5 <= enemy.rad + bullet.rad:
                enemyList.remove(enemy)
                playerBulletList.remove(bullet)
                break
    
    for bullet in enemyBulletList:
        if ((bullet.x - posx)**2 + (bullet.y - posy)**2)**0.5 <= rad + bullet.rad:
            hp -= 1
            enemyBulletList.remove(bullet)

    if hp <= 0:
        running = False

    pygame.draw.circle(screen, playerColor, (posx, posy), rad)
    pygame.display.update()

print("게임 종료")