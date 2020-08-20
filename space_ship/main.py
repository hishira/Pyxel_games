import pyxel

class Bullet:
    def __init__(self):
        self.bullets = []
    
    def createBullet(self,x,y):
        self.bullets.append([x,y])
    
    def updateBulletMovement(self):
        for i in self.bullets:
            i[1]-=6

    def drawBullets(self):
        for i in self.bullets:
            pyxel.line(i[0],i[1],i[0],i[1]+3,1)   
class Ship:
    def __init__(self):
        self.blocks = [[80,110,4],[84,110,4],[76,110,4],[80,106,4]]
        self.bullets = Bullet()

    def draw(self):
        for i in self.blocks:
            pyxel.rect(i[0],i[1],i[2],i[2],1)
    
    def checkShot(self):
        if pyxel.btnp(pyxel.KEY_SPACE,hold=1,period=1):
            self.bullets.createBullet(self.blocks[3][0],self.blocks[3][1])

    def shipMovement(self):
        print(pyxel.frame_count)
        if pyxel.btnp(pyxel.KEY_LEFT,hold=1,period=1):
            for i in self.blocks:
                i[0] -= 4 
        if pyxel.btnp(pyxel.KEY_RIGHT,hold=1,period=1):
            for i in self.blocks:
                i[0] += 4 

class App:
    def __init__(self):
        self.ship = Ship()
        pyxel.init(150,120,quit_key=pyxel.KEY_Q)
        pyxel.run(self.update,self.draw)
        
    def update(self):
        self.ship.shipMovement()
        self.ship.checkShot()
        self.ship.bullets.updateBulletMovement()
    
    def draw(self):
        pyxel.cls(5)
        self.ship.draw()
        self.ship.bullets.drawBullets()

App()