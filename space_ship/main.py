import pyxel
from random import randint


WIDTH = 150
HEIGHT = 120
GAME_POINT = 0.0
SHIP_LIFE = 10
BOSS_LIFE = 30
BOSS_SHOT_DENSITY = 50
class Bullet:
    def __init__(self):
        self.bullets = []
        self.bulletWidth = 1
        self.bulletHeight = 3

    def createBullet(self,x,y):
        self.bullets.append([x,y])
    
    def updateBulletMovement(self):
        for i in self.bullets:
            i[1]-=2

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
        self.firstWaveAlienBullet = []

    def createFirstWaveShip(self):
        firstX = randint(10,WIDTH - 10)
        firstY = self.lastPositionY + 5
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
                i[0] += 3
            else:
                i[0] -= 2
    
    def bulletFirstWaveAlienShip(self):
        chooser = randint(0,20)
        if chooser < 10:
            self.firstWaveAlienBullet.append([self.firstWaveAlienShip[0][0] + 2,self.firstWaveAlienShip[0][1] + 2])
        else:
            self.firstWaveAlienBullet.append([self.firstWaveAlienShip[1][0] + 2,self.firstWaveAlienShip[1][1] + 2])
    
    def updateFirstAlienWAveMovement(self):
        for i in self.firstWaveAlienBullet:
            i[1] += 1
    
    def resetAlienFirstWave(self):
        self.firstWave = []

    def drawAlienFirstWaveBullet(self):
        for i in self.firstWaveAlienBullet:
            pyxel.line(i[0],i[1],i[0],i[1] + 2,4)

    def drawFirstWaveAlienShip(self):
        for i in self.firstWaveAlienShip:
            pyxel.tri(i[0],i[1],i[0] + 2,i[1] + 2,i[0] + 4,i[1],4)
    
    def getFirstAlienBulletWave(self):
        return self.firstWaveAlienBullet
    
    def removeAlienFirstWaveBullet(self):
        self.firstWaveAlienBullet = []

    def removeFirstWaveAlienBullet(self,index):
        return self.firstWaveAlienBullet.pop(index)

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
    
    def getFirstWaveLength(self):
        return len(self.firstWave)

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
        self.blocks = [[80,110,3],[83,110,3],[77,110,3],[80,107,3]]
        self.bullets = Bullet()

    def draw(self):
        for i in self.blocks:
            pyxel.rect(i[0],i[1],i[2],i[2],1)
    
    def checkShot(self):
        if pyxel.btnp(pyxel.KEY_SPACE,hold=3,period=3):
            self.bullets.createBullet(self.blocks[3][0],self.blocks[3][1])

    def getShipPossition(self):
        return self.blocks
        
    def shipMovement(self):
        print(pyxel.frame_count)
        if pyxel.btnp(pyxel.KEY_LEFT,hold=1,period=1):
            for i in self.blocks:
                i[0] -= 1 * 3 #(pyxel.frame_count % 7)
        if pyxel.btnp(pyxel.KEY_RIGHT,hold=1,period=1):
            for i in self.blocks:
                i[0] += 1 * 3#(pyxel.frame_count % 7)

class Boss:
    
    def __init__(self):
        pyxel.image(0).load(20,20,"boss.png")
        self.bossMovement = "R"
        self.x = 5
        self.y = 5
        self.bossBullets = []
        self.bossBullet = 0

    def getBossPosition(self):
        return [(self.x,self.y)]

    def draw(self):
        pyxel.blt(self.x,self.y,0,20,20,20,20,0)
        self.drawBossBullet()

    def getBossBullet(self):
        return self.bossBullets
    
    def removeBossBullet(self,index):
        self.bossBullets.pop(index)

    def bossUpdate(self):
        global BOSS_SHOT_DENSITY
        self.bossMovementUpdate()
        if self.getNumberOfBossBullet() > 10:
            BOSS_SHOT_DENSITY = 10
        elif self.getNumberOfBossBullet() > 20:
            BOSS_SHOT_DENSITY = 5
        if pyxel.frame_count % BOSS_SHOT_DENSITY == 0:
            self.createBossShot()
        
    def drawBossBullet(self):
        for i in self.bossBullets:
            pyxel.line(i[0],i[1],i[0],i[1]+3,7)

    def bossMovementUpdate(self):
        print(self.x)
        if self.x > pyxel.width - 20:
            self.bossMovement = "L"
        elif self.x < 5:
            self.bossMovement = "R"
        if self.bossMovement == "R":
            self.x += 4 % (pyxel.frame_count + 1)
        else:
            self.x -= 4 % (pyxel.frame_count + 1)
        self.updateBossBulletMovement()

    def createBossShot(self):
        self.bossBullets.append([self.x+10,self.y+15])
        self.bossBullet+=1
    
    def getNumberOfBossBullet(self):
        return self.bossBullet

    def updateBossBulletMovement(self):
        for i in self.bossBullets:
            i[1]+=2
class App:
    def __init__(self):
        self.ship = Ship()
        self.alien = Alien()
        self.alien.createFirstWave()
        self.alien.createFirstWaveShip()
        self.game_over = False
        self.userRestartChoice = "YES"
        self.bossStage = False
        pyxel.init(WIDTH,HEIGHT,quit_key=pyxel.KEY_Q)
        self.boss = Boss()
        pyxel.run(self.update,self.draw)
 
    def update(self):
        if self.bossStage:
            global BOSS_LIFE
            self.boss.bossUpdate()
            self.collisionBossShipBullet()
            self.ship.shipMovement()
            self.ship.checkShot()
            self.ship.bullets.updateBulletMovement()
            if pyxel.frame_count % 50 == 0:
                self.ship.bullets.removeUnusedBullets()
            self.collisionShipBulletBoss()
            if BOSS_LIFE == 0:
                pyxel.quit()
        else:
            self.ship.shipMovement()
            self.ship.checkShot()
            self.checkCollisionBulletBlock()
            self.ship.bullets.updateBulletMovement()
            self.alien.firstWaveShipMovement()
            if pyxel.frame_count % 10 == 0:
                self.alien.bulletFirstWaveAlienShip()
            self.alien.updateFirstAlienWAveMovement()
            if pyxel.frame_count % 50 == 0:
                self.ship.bullets.removeUnusedBullets()
            self.checkCollisionBulletShip()
            if self.alien.getFirstWaveLength() == 0:
                self.bossStage = True
    
        

    def checkCollisionBlock(self,rect1x,rect1y,rect1width,rect1height,
                            rect2x,rect2y,rect2width,rect2height):
        if (rect1x < rect2x + rect2width and
            rect1x + rect1width > rect2x and
            rect1y < rect2y + rect2height and
            rect1y + rect1height > rect2y):
            return True
        return False

    def collisionShipBulletBoss(self):
        counter = 0
        for i in self.ship.bullets.getBulletPosition():
            for j in self.boss.getBossPosition():
                if self.checkCollisionBlock(i[0],i[1],1,2,j[0],j[1],20,20):
                    global BOSS_LIFE
                    BOSS_LIFE-=1
                    return
    def collisionBossShipBullet(self):
        counter = 0
        for i in self.boss.getBossBullet():
            for j in self.ship.getShipPossition():
                if self.checkCollisionBlock(i[0],i[1],1,3,j[0],j[1],3,3):
                    global SHIP_LIFE
                    SHIP_LIFE -= 1
                    if SHIP_LIFE == 0:
                        self.game_over = True
                    self.boss.removeBossBullet(counter)
                    return
            counter+=1

    def checkCollisionBulletShip(self):
        counter = 0
        for i in self.alien.getFirstAlienBulletWave():
            for j in self.ship.getShipPossition():
                if self.checkCollisionBlock(i[0],i[1],1,2,j[0],j[1],3,3):
                    global SHIP_LIFE
                    SHIP_LIFE-=1
                    if SHIP_LIFE == 0:
                        self.game_over = True
                    self.alien.removeFirstWaveAlienBullet(counter)
                    return
            counter+=1


    def checkCollisionBulletBlock(self):
        alien_counter = 0
        bullet_counter = 0
        for i in self.ship.bullets.getBulletPosition():
            for j in self.alien.getFirstWavePositions():    
                if self.checkCollisionBlock(i[0],i[1],self.ship.bullets.getBulletWidht(),self.ship.bullets.getBulletHeight(),
                        j[0],j[1],self.alien.getFirstWaveWidth(),self.alien.getFirstWaveHieght()):
                        self.ship.bullets.bulletRemove(bullet_counter)
                        self.alien.setLifeFirstWave(alien_counter,self.alien.getLifeOfFirstWave(alien_counter) - 1)
                        global GAME_POINT
                        GAME_POINT += 0.4
                        if self.alien.getLifeOfFirstWave(alien_counter) == 0:
                            self.alien.firstWaveRemove(alien_counter)
                        return
                alien_counter+=1
            bullet_counter+=1
            alien_counter = 0
        print("Pociski : " + str(len(self.ship.bullets.getBulletPosition())))

    def drawGameMode(self):
        self.ship.draw()
        self.ship.bullets.drawBullets()
        self.alien.drawFirstWave()
        self.alien.drawFirstWaveAlienShip()
        self.alien.drawAlienFirstWaveBullet()
        pyxel.text(0,115,"{0:02f}".format(GAME_POINT),1)
        pyxel.text(140,115,"{}".format(SHIP_LIFE),1)

    def drawBossStage(self):
        self.ship.draw()
        self.ship.bullets.drawBullets()
        self.boss.draw()
        pyxel.text(140,115,"{}".format(SHIP_LIFE),1)
        pyxel.text(140,0,"{}".format(BOSS_LIFE),1)

    def resetGame(self):
        self.alien.resetAlienFirstWave()
        self.alien.createFirstWave()
        global SHIP_LIFE
        SHIP_LIFE = 3
        self.alien.removeAlienFirstWaveBullet()

    def userChoiceRestartChange(self):
        if pyxel.btnp(pyxel.KEY_RIGHT):
            self.userRestartChoice = "NO"
        if pyxel.btnp(pyxel.KEY_LEFT):
            self.userRestartChoice = "YES"
        if pyxel.btnp(pyxel.KEY_ENTER):
            if self.userRestartChoice == "YES":
                self.game_over = False
                self.resetGame()
            else:
                pyxel.quit()
                
    def draw(self):
        pyxel.cls(5)
        if not self.game_over and self.bossStage == False:
            self.drawGameMode()
        elif self.bossStage:
            self.drawBossStage()
        else:
            self.userChoiceRestartChange()
            pyxel.text(58,55,"GAME OVER",9)
            pyxel.text(60,65,"RESTART?",9)
            pyxel.text(58,75,"YES    NO",9)
            if self.userRestartChoice == "YES":
                pyxel.rectb(55,73,15,9,6)
            else:
                pyxel.rectb(80,73,15,9,6)

App()