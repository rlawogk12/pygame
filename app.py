import pygame
import os
import random
import math

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
rad = 14
playerColor = (102, 255, 102)
hp = 20000000
speed  = 3
engage = 5

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
            if event.key == pygame.K_a:
                if engage > 0:
                    enemyBulletList.clear()
                    engage -= 1
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
        playerBulletList.append(Bullet(posx-10, posy - rad, playerBulletColor, -0.5, -9))
        playerBulletList.append(Bullet(posx, posy - rad, playerBulletColor, 0, -9))
        playerBulletList.append(Bullet(posx+10, posy - rad, playerBulletColor, 0.5, -9))

    for bullet in playerBulletList:
        pygame.draw.circle(screen, bullet.color, (bullet.x, bullet.y), bullet.rad)
        playerBulletList = bullet.update(playerBulletList)

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
    if frame_tick == 500:
        enemyList.append(Enemy(50, 0, (255,80,0), 0, 1.5, etype=1))
    if frame_tick == 520:
        enemyList.append(Enemy(SCREEN_WIDTH-50, 0, (255,80,0), 0, 1.5, etype=1))
    if frame_tick == 540:
        enemyList.append(Enemy(SCREEN_WIDTH//2, 0, (255,80,0), 0, 1.5, etype=1))
    if frame_tick == 560:
        enemyList.append(Enemy(random.randint(16, SCREEN_WIDTH-16), 0, (255,80,0), 0, 1.5, etype=2))
    if frame_tick == 580:
        enemyList.append(Enemy(random.randint(16, SCREEN_WIDTH-16), 0, (255,80,0), 0, 1.5, etype=2))
    if frame_tick == 600:
        enemyList.append(Enemy(random.randint(16, SCREEN_WIDTH-16), 0, (255,80,0), 0, 1.5, etype=2))
    # boss
    if frame_tick >= 710:
        for e in enemyList:
            if e.etype == 3:
                cur = e.rad * 2 * e.hp / 3800
                pygame.draw.rect(screen, (255,0,0), [e.x-e.rad, e.y-e.rad-20, cur, 4])
    if frame_tick == 700:
        enemyList.append(Enemy(SCREEN_WIDTH//2, 0, (200, 0, 0), 0, 5, etype=3))
        for e in enemyList:
            if e.etype == 3:
                e.rad = 40
                e.hp = 3800
    if frame_tick >= 900:
        if frame_tick % 300 == 0:
            for e in enemyList:
                if e.etype == 3:
                    e.xspeed = random.randint(-30, 30)/10
                    e.yspeed = random.randint(-30, 30)/10
    if frame_tick == 780:
        enemyBulletList.append(Bullet(SCREEN_WIDTH//5, 0, (200, 0, 0), 0, 0, case=3, rad=10))
        enemyBulletList.append(Bullet(SCREEN_WIDTH//5*2, 0, (200, 0, 0), 0, 0, case=3, rad=10))
        enemyBulletList.append(Bullet(SCREEN_WIDTH//5*3, 0, (200, 0, 0), 0, 0, case=3, rad=10))
        enemyBulletList.append(Bullet(SCREEN_WIDTH//5*4, 0, (200, 0, 0), 0, 0, case=3, rad=10))
    if 800 <= frame_tick <= 1100:
        if frame_tick % 5 == 0:
            enemyBulletList.append(Bullet(SCREEN_WIDTH//5, 0, (200, 0, 0), 0, 4))
            enemyBulletList.append(Bullet(SCREEN_WIDTH//5*2, 0, (200, 0, 0), 0, 4))
            enemyBulletList.append(Bullet(SCREEN_WIDTH//5*3, 0, (200, 0, 0), 0, 4))
            enemyBulletList.append(Bullet(SCREEN_WIDTH//5*4, 0, (200, 0, 0), 0, 4))
    if frame_tick == 1280:
        enemyBulletList.append(Bullet(SCREEN_WIDTH//6, SCREEN_HEIGHT, (200, 0, 0), 0, 0, case=3, rad=10))
        enemyBulletList.append(Bullet(SCREEN_WIDTH//6*2, SCREEN_HEIGHT, (200, 0, 0), 0, 0, case=3, rad=10))
        enemyBulletList.append(Bullet(SCREEN_WIDTH//6*3, SCREEN_HEIGHT, (200, 0, 0), 0, 0, case=3, rad=10))
        enemyBulletList.append(Bullet(SCREEN_WIDTH//6*4, SCREEN_HEIGHT, (200, 0, 0), 0, 0, case=3, rad=10))
        enemyBulletList.append(Bullet(SCREEN_WIDTH//6*5, SCREEN_HEIGHT, (200, 0, 0), 0, 0, case=3, rad=10))
    if 1300 <= frame_tick <= 1600:
        if frame_tick % 5 == 0:
            enemyBulletList.append(Bullet(SCREEN_WIDTH//6, SCREEN_HEIGHT, (200, 0, 0), 0, -4))
            enemyBulletList.append(Bullet(SCREEN_WIDTH//6*2, SCREEN_HEIGHT, (200, 0, 0), 0, -4))
            enemyBulletList.append(Bullet(SCREEN_WIDTH//6*3, SCREEN_HEIGHT, (200, 0, 0), 0, -4))
            enemyBulletList.append(Bullet(SCREEN_WIDTH//6*4, SCREEN_HEIGHT, (200, 0, 0), 0, -4))
            enemyBulletList.append(Bullet(SCREEN_WIDTH//6*5, SCREEN_HEIGHT, (200, 0, 0), 0, -4))
    if frame_tick == 880:
        enemyBulletList.append(Bullet(0, SCREEN_HEIGHT//10*1, (200, 0, 0), 0, 0, case=3, rad=10))
        enemyBulletList.append(Bullet(0, SCREEN_HEIGHT//10*2, (200, 0, 0), 0, 0, case=3, rad=10))
        enemyBulletList.append(Bullet(0, SCREEN_HEIGHT//10*3, (200, 0, 0), 0, 0, case=3, rad=10))
        enemyBulletList.append(Bullet(0, SCREEN_HEIGHT//10*4, (200, 0, 0), 0, 0, case=3, rad=10))
        enemyBulletList.append(Bullet(0, SCREEN_HEIGHT//10*5, (200, 0, 0), 0, 0, case=3, rad=10))
        enemyBulletList.append(Bullet(0, SCREEN_HEIGHT//10*6, (200, 0, 0), 0, 0, case=3, rad=10))
        enemyBulletList.append(Bullet(0, SCREEN_HEIGHT//10*7, (200, 0, 0), 0, 0, case=3, rad=10))
        enemyBulletList.append(Bullet(0, SCREEN_HEIGHT//10*8, (200, 0, 0), 0, 0, case=3, rad=10))
        enemyBulletList.append(Bullet(0, SCREEN_HEIGHT//10*9, (200, 0, 0), 0, 0, case=3, rad=10))
    if 900 <= frame_tick <= 1200:
        if frame_tick % 5 == 0:
            enemyBulletList.append(Bullet(0, SCREEN_HEIGHT//10, (200, 0, 0), 4, 0))
            enemyBulletList.append(Bullet(0, SCREEN_HEIGHT//10*2, (200, 0, 0), 4, 0))
            enemyBulletList.append(Bullet(0, SCREEN_HEIGHT//10*3, (200, 0, 0), 4, 0))
            enemyBulletList.append(Bullet(0, SCREEN_HEIGHT//10*4, (200, 0, 0), 4, 0))
            enemyBulletList.append(Bullet(0, SCREEN_HEIGHT//10*5, (200, 0, 0), 4, 0))
            enemyBulletList.append(Bullet(0, SCREEN_HEIGHT//10*6, (200, 0, 0), 4, 0))
            enemyBulletList.append(Bullet(0, SCREEN_HEIGHT//10*7, (200, 0, 0), 4, 0))
            enemyBulletList.append(Bullet(0, SCREEN_HEIGHT//10*8, (200, 0, 0), 4, 0))
            enemyBulletList.append(Bullet(0, SCREEN_HEIGHT//10*9, (200, 0, 0), 4, 0))
    if frame_tick == 1380:
        enemyBulletList.append(Bullet(SCREEN_WIDTH, SCREEN_HEIGHT//10*1, (200, 0, 0), 0, 0, case=3, rad=10))
        enemyBulletList.append(Bullet(SCREEN_WIDTH, SCREEN_HEIGHT//10*2, (200, 0, 0), 0, 0, case=3, rad=10))
        enemyBulletList.append(Bullet(SCREEN_WIDTH, SCREEN_HEIGHT//10*3, (200, 0, 0), 0, 0, case=3, rad=10))
        enemyBulletList.append(Bullet(SCREEN_WIDTH, SCREEN_HEIGHT//10*4, (200, 0, 0), 0, 0, case=3, rad=10))
        enemyBulletList.append(Bullet(SCREEN_WIDTH, SCREEN_HEIGHT//10*5, (200, 0, 0), 0, 0, case=3, rad=10))
        enemyBulletList.append(Bullet(SCREEN_WIDTH, SCREEN_HEIGHT//10*6, (200, 0, 0), 0, 0, case=3, rad=10))
        enemyBulletList.append(Bullet(SCREEN_WIDTH, SCREEN_HEIGHT//10*7, (200, 0, 0), 0, 0, case=3, rad=10))
        enemyBulletList.append(Bullet(SCREEN_WIDTH, SCREEN_HEIGHT//10*8, (200, 0, 0), 0, 0, case=3, rad=10))
        enemyBulletList.append(Bullet(SCREEN_WIDTH, SCREEN_HEIGHT//10*9, (200, 0, 0), 0, 0, case=3, rad=10))
    if 1400 <= frame_tick <= 1700:
        if frame_tick % 5 == 0:
            enemyBulletList.append(Bullet(SCREEN_WIDTH, SCREEN_HEIGHT//10*1, (200, 0, 0), -4, 0))
            enemyBulletList.append(Bullet(SCREEN_WIDTH, SCREEN_HEIGHT//10*2, (200, 0, 0), -4, 0))
            enemyBulletList.append(Bullet(SCREEN_WIDTH, SCREEN_HEIGHT//10*3, (200, 0, 0), -4, 0))
            enemyBulletList.append(Bullet(SCREEN_WIDTH, SCREEN_HEIGHT//10*4, (200, 0, 0), -4, 0))
            enemyBulletList.append(Bullet(SCREEN_WIDTH, SCREEN_HEIGHT//10*5, (200, 0, 0), -4, 0))
            enemyBulletList.append(Bullet(SCREEN_WIDTH, SCREEN_HEIGHT//10*6, (200, 0, 0), -4, 0))
            enemyBulletList.append(Bullet(SCREEN_WIDTH, SCREEN_HEIGHT//10*7, (200, 0, 0), -4, 0))
            enemyBulletList.append(Bullet(SCREEN_WIDTH, SCREEN_HEIGHT//10*8, (200, 0, 0), -4, 0))
            enemyBulletList.append(Bullet(SCREEN_WIDTH, SCREEN_HEIGHT//10*9, (200, 0, 0), -4, 0))
    if frame_tick >= 1750:
        std = frame_tick % 360
        degrees = list(range(std, std+360, 72))
        for b in enemyBulletList:
            if b.case == 9:
                enemyBulletList.remove(b)
        for e in enemyList:
            if e.etype == 3:
                for val in degrees:
                    enemyBulletList.append(Bullet(e.x + math.sin(math.pi*(val/180))*70, e.y + math.cos(math.pi*(val/180))*70, (200, 0, 0), 0, 0, case=9))
                for b in enemyBulletList:
                    if b.case == 9:
                        b.rad = 10
    if 1760 <= frame_tick :
        if frame_tick % 20 == 0:
            for b in enemyBulletList:
                if b.case == 9:
                    enemyBulletList.append(Bullet(b.x, b.y, (255, 255, 0), (posx-b.x)/80, (posy-b.y)/80))
    if 1800 <= frame_tick :
        if frame_tick % 200 == 0:
            for e in enemyList:
                if e.etype == 3:
                    enemyList.append(Enemy(e.x, e.y, (255,255,0), 0, 1.5, etype=1))
                if e.etype == 1:
                    e.hp = 10
    if frame_tick >= 1500:
        if len(enemyList) == 0:
            running = False
            print("스테이지 클리어")
    
    # 잡몹 draw
    for enemy in enemyList:
        pygame.draw.circle(screen, enemy.color, (enemy.x, enemy.y), enemy.rad)
        enemyBulletList = enemy.update(enemyBulletList)
    
    for bullet in enemyBulletList:
        pygame.draw.circle(screen, bullet.color, (bullet.x, bullet.y), bullet.rad)
        enemyBulletList = bullet.update(enemyBulletList)

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
                enemy.hp -= 1
                playerBulletList.remove(bullet)
                if enemy.hp <= 0:    
                    enemyList.remove(enemy)
                    break
    
    for bullet in enemyBulletList:
        if ((bullet.x - posx)**2 + (bullet.y - posy)**2)**0.5 <= rad + bullet.rad:
            hp -= 1
            enemyBulletList.remove(bullet)

    if hp <= 0:
        running = False

    pygame.draw.circle(screen, playerColor, (posx, posy), rad)
    pygame.display.update()

for e in enemyList:
    print("남은 적의 체력:", e.hp)

print("게임 종료")