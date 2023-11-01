class Bullet:
    def __init__(self, x, y, color, xspeed, yspeed) -> None:
        self.x = x
        self.y = y
        self.rad = 4
        self.color = color
        self.xspeed = xspeed
        self.yspeed = yspeed

    def update(self):
        self.x += self.xspeed
        self.y += self.yspeed