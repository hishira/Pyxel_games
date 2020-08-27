import pyxel
from random import randint


WIDTH = 150
HEIGHT = 120
class Bullet:
    def __init__(self):
        self.bullets = []
        self.bulletWidth = 1
        self.bulletHeight = 3

    def createBullet(self,x,y):
        self.bullets.append([x,y])
    
    def updateBulletMovement(self):
        for i in self.bullets:
            i[1]-=6

    def getBulletWidht(self):
        return self.bulletWidth

    def getBulletHeight(self):
        return self.bulletHeight
    
    def drawBullets(self):
        for i in self.bullets:
            pyxel.line(i[0],i[1],i[0],i[1]+3,1)
    
    def getBulletPosition(self):
        return self.bullets

    def bulletRemove(self,index):
        self.bullets.pop(index)
    
    def removeUnusedBullets(self):
        counter = 0
        for i in self.getBulletPosition():
            if i[1] < 0:
                self.bulletRemove(counter)
                counter-=1
            counter+=1

class Alien:
    def __init__(self):
        self.firstWave = []
        self.firstWaveWidth = 4
        self.firstWaveHeight = 2
        self.firstWaveAlienShip = []
        self.lastPositionY = 0

    def createFirstWaveShip(self):
        firstX = randint(10,WIDTH - 10)
        firstY = self.lastPositionY
        self.firstWaveAlienShip.append([firstX,firstY,"R"])
        secodX = randint(10,WIDTH - 10)
        while (secodX < firstX + 4 and secodX > firstX - 4)  or secodX == firstX:
            secodX = randint(10,WIDTH - 10)
        self.firstWaveAlienShip.append([secodX,firstY,"R"])
    
    def firstWaveShipMovement(self):
        for i in self.firstWaveAlienShip:
            if i[0] > WIDTH - 5 and i[2] == "R":
                i[2] = "L"
            elif i[0] <= 0 and i[2] == "L":
                i[2] = "R"
            elif i[2]  == "R":
                i[0] += 2
            else:
                i[0] -= 2

    def drawFirstWaveAlienShip(self):
        for i in self.firstWaveAlienShip:
            pyxel.tri(i[0],i[1],i[0] + 2,i[1] + 2,i[0] + 4,i[1],4)
    
    def createFirstWave(self):
        x = 6
        y = 5
        betpas = 2
        for i in range(80):
            self.firstWave.append([x,y,4])
            x += 5 + betpas
            if i == 19:
                y+=5
                x = 6
            elif i == 39:
                y+=5
                x = 6
            elif i == 59:
                y+=5
                x = 6
        self.lastPositionY = y + 5
    
    def getFirstWavePositions(self):
        return self.firstWave
    
    def getFirstWaveWidth(self):
        return self.firstWaveWidth
    
    def getFirstWaveHieght(self):
        return self.firstWaveHeight

    def firstWaveRemove(self,index):
        self.firstWave.pop(index)
    
    def getLifeOfFirstWave(self,index):
        return self.firstWave[index][2]
    
    def setLifeFirstWave(self,index,value):
        self.firstWave[index][2] = value

    def drawFirstWave(self):
        for i in self.firstWave:
            if i[2] <= 2:
                pyxel.rect(i[0],i[1],self.firstWaveWidth - 1,self.firstWaveHeight ,1)
            else:    
                pyxel.rect(i[0],i[1],self.firstWaveWidth,self.firstWaveHeight,1)
class Ship:
    def __init__(self):
        self.blocks = [[80,110,4],[84,110,4],[76,110,4],[80,106,4]]
        self.bullets = Bullet()

    def draw(self):
        for i in self.blocks:
            pyxel.rect(i[0],i[1],i[2],i[2],1)
    
    def checkShot(self):
        if pyxel.btnp(pyxel.KEY_SPACE,hold=3,period=3):
            self.bullets.createBullet(self.blocks[3][0],self.blocks[3][1])

    def shipMovement(self):
        print(pyxel.frame_count)
        if pyxel.btnp(pyxel.KEY_LEFT,hold=1,period=1):
            for i in self.blocks:
                i[0] -= 1 * 3 #(pyxel.frame_count % 7)
        if pyxel.btnp(pyxel.KEY_RIGHT,hold=1,period=1):
            for i in self.blocks:
                i[0] += 1 * 3#(pyxel.frame_count % 7)

class App:
    def __init__(self):
        self.ship = Ship()
        self.alien = Alien()
        self.alien.createFirstWave()
        self.alien.createFirstWaveShip()
        pyxel.init(WIDTH,HEIGHT,quit_key=pyxel.KEY_Q)
        pyxel.run(self.update,self.draw)
        
    def update(self):
        self.ship.shipMovement()
        self.ship.checkShot()
        self.ship.bullets.updateBulletMovement()
        self.checkCollisionBulletBlock()
        self.alien.firstWaveShipMovement()

        if pyxel.frame_count % 50 == 0:
            self.ship.bullets.removeUnusedBullets()
    
    def checkCollisionBlock(self,rect1x,rect1y,rect1width,rect1height,
                            rect2x,rect2y,rect2width,rect2height):
        if (rect1x < rect2x + rect2width and
            rect1x + rect1width > rect2x and
            rect1y < rect2y + rect2height and
            rect1y + rect1height > rect2y):
            return True
        return False

    def checkCollisionBulletBlock(self):
        alien_counter = 0
        bullet_counter = 0
        for i in self.ship.bullets.getBulletPosition():
            for j in self.alien.getFirstWavePositions():    
                if self.checkCollisionBlock(i[0],i[1],self.alien.getFirstWaveWidth(),self.alien.getFirstWaveHieght(),
                        j[0],j[1],self.ship.bullets.getBulletWidht(),self.ship.bullets.getBulletHeight()):
                        self.ship.bullets.bulletRemove(bullet_counter)
                        self.alien.setLifeFirstWave(alien_counter,self.alien.getLifeOfFirstWave(alien_counter) - 1)
                        if self.alien.getLifeOfFirstWave(alien_counter) == 0:
                            self.alien.firstWaveRemove(alien_counter)
                        return
                alien_counter+=1
            bullet_counter+=1
            alien_counter = 0
        print("Pociski : " + str(len(self.ship.bullets.getBulletPosition())))

    def draw(self):
        pyxel.cls(5)
        self.ship.draw()
        self.ship.bullets.drawBullets()
        self.alien.drawFirstWave()
        self.alien.drawFirstWaveAlienShip()
App()