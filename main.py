import pyxel
WIDTH = 160
HEIGHT = 120
DIRECTION = "N"
class App:
    def __init__(self):
        pyxel.init(WIDTH,HEIGHT,quit_key=pyxel.KEY_Q)
        self.x = WIDTH / 2
        self.y = HEIGHT / 2
        self.direction = DIRECTION
        pyxel.run(self.update,self.draw)
    
    def update(self):
        if self.direction == "N":
            self.y = (self.y - 1) % pyxel.height
        elif self.direction == "E":
            self.x = (self.x + 1) % pyxel.width
        elif self.direction == "S":
            self.y = (self.y + 1) % pyxel.height
        else:
            self.x = (self.x - 1) % pyxel.width
        self.movementCheck()

    def movementCheck(self):
        if pyxel.btnp(pyxel.KEY_LEFT):
            self.direction = "W"
            print("OK")
        if pyxel.btnp(pyxel.KEY_RIGHT):
            self.direction = "E"
        if pyxel.btnp(pyxel.KEY_UP):
            self.direction = "N"
        if pyxel.btnp(pyxel.KEY_DOWN):
            self.direction = "S"
    
    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.x,self.y,4,4,4)
        

App()