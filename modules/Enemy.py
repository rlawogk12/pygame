from .Bullet import Bullet
import random

class Enemy:
    def __init__(self, x, y, color, xspeed, yspeed, etype = 0) -> None:
        self.x = x
        self.y = y
        self.rad = 16
        self.color = color
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.etype = etype
        self.tick = 0
        self.shooting_state = random.randint(80, 160)
        self.hp = 1

    def update(self, bulletList=[]):
        if self.etype == 0:
            self.update_pattern1()
        elif self.etype == 1:
            bulletList = self.update_pattern2(bulletList)
        elif self.etype == 2:
            bulletList = self.update_pattern3(bulletList)
        elif self.etype == 3:
            self.update_boss_pattern1()
        return bulletList

    def update_boss_pattern1(self):
        self.tick += 1
        self.x += self.xspeed
        self.y += self.yspeed

        self.xspeed *= 0.95
        self.yspeed *= 0.95

        if self.tick > 60:
            if self.x <= self.rad*2: self.x = self.rad*2
            if self.x+self.rad*2 >= 320: self.x = 320-self.rad*2
            if self.y <= self.rad*2: self.y = self.rad*2
            if self.y >= 160: self.y = 160


    def update_pattern1(self):
        self.x += self.xspeed
        self.y += self.yspeed
        self.yspeed += 0.02

    def update_pattern2(self, bulletList):
        self.tick += 1
        self.x += self.xspeed
        self.y += self.yspeed
        self.yspeed -= 0.02
        newList = bulletList
        if self.tick == 50:
            newList.append(Bullet(self.x, self.y, (255, 80, 0), 0, 6, rad=20, case=2))
        return newList

    def update_pattern3(self, bulletList):
        self.tick += 1
        self.x += self.xspeed
        self.y += self.yspeed
        newList = bulletList
        if self.tick == self.shooting_state:
            newList.append(Bullet(self.x, self.y, (255, 80, 0), -6, 0, rad=20, case=2))
            newList.append(Bullet(self.x, self.y, (255, 80, 0), 6, 0, rad=20, case=2))
        return newList