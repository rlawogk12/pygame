class Enemy:
    def __init__(self, x, y, color, xspeed, yspeed) -> None:
        self.x = x
        self.y = y
        self.rad = 16
        self.color = color
        self.xspeed = xspeed
        self.yspeed = yspeed

    def update_pattern1(self):
        self.x += self.xspeed
        self.y += self.yspeed
        self.yspeed += 0.02