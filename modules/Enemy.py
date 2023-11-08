from .Bullet import Bullet

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

    def update(self, bulletList=[]):
        if self.etype == 0:
            self.update_pattern1()
        if self.etype == 1:
            bulletList = self.update_pattern2(bulletList)
        return bulletList

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
