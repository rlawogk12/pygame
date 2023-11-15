import math

class Bullet:
    def __init__(self, x, y, color, xspeed, yspeed, rad=4, case=1) -> None:
        self.x = x
        self.y = y
        self.rad = rad
        self.color = color
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.case = case
        self.tick = 0
        self.w = 320
        self.h = 640

    def update(self, bulletList):
        if self.case == 1:
            self.case1()
        elif self.case == 2:
            bulletList = self.case2(bulletList)
        elif self.case == 3:
            bulletList = self.case3(bulletList)
        return bulletList
    
    def case1(self):
        self.x += self.xspeed
        self.y += self.yspeed

    def case2(self, bulletList):
        newList = bulletList
        self.tick += 1
        self.x += self.xspeed
        self.y += self.yspeed
        if self.x < self.rad or self.x + self.rad > self.w or self.y < self.rad or self.y + self.rad > self.h:
            degrees = [-150, -120, -90, -60, -30, 0, 30, 60, 90, 120, 150, 180]
            for val in degrees:
                newList.append(Bullet(self.x, self.y, (255, 80, 0), math.sin(math.pi*(val/180))*1.0, math.cos(math.pi*(val/180))*1))
                newList.append(Bullet(self.x, self.y, (255, 80, 0), math.sin(math.pi*(val/180))*1.5, math.cos(math.pi*(val/180))*1.5))
            newList.remove(self)
        return newList
    
    def case3(self, bulletList):
        self.tick += 1
        newList = bulletList
        if self.tick >= 300:
            newList.remove(self)
        return newList
    