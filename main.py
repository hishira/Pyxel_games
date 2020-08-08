import pyxel
from random import randint

WIDTH = 160
HEIGHT = 120
DIRECTION = "N"
class App:
    def __init__(self):
        pyxel.init(WIDTH,HEIGHT,quit_key=pyxel.KEY_Q)
        self.x = WIDTH / 2
        self.y = HEIGHT / 2
        self.direction = DIRECTION
        self.numberOfFood = 0
        self.food = []
        self.snakeParts = []
        self.snakeParts.append([self.x,self.y])
        pyxel.run(self.update,self.draw)
    
    def update(self):
        if self.direction == "N":
            self.snakeUpdateMovement("N")
        elif self.direction == "E":
            self.snakeUpdateMovement("E")
        elif self.direction == "S":
            self.snakeUpdateMovement("S")
        else:
            self.snakeUpdateMovement("W")
        self.movementCheck()
        self.checkCollisionSnakeWithFood()
        self.checkFoodAndUpdate()

    def snakeUpdateMovement(self,direction):
        if direction == "N":
            for i in self.snakeParts:
                i[1] = (i[1] - 1) % pyxel.height
        elif direction == "E":
            for i in self.snakeParts:
                i[0] = (i[0] + 1) % pyxel.width
        elif direction == "S":
            for i in self.snakeParts:
                i[1] = (i[1] + 1) % pyxel.height
        else:
            for i in self.snakeParts:
                i[0] = (i[0] - 1) % pyxel.width

    def collisionStatement(self,foodx,foody,snakeheadx,snakeheady,foodWidht,snakeWidht):
        if (foodx < snakeheadx + snakeWidht and 
        foodx + foodWidht > snakeheadx and foody < snakeheady +snakeWidht and
        foody + foodWidht > snakeheady):
            return True 
        return False 
    def checkCollisionSnakeWithFood(self):
        count = 0
        for i in self.food:
            if self.collisionStatement(i[0],i[1],self.snakeParts[0][0],self.snakeParts[0][1],1.5,4):
                del self.food[count]
                print("Collision")
                break
            count+=1

    def checkFoodAndUpdate(self):
        if self.numberOfFood == 0 or self.numberOfFood < 5:
            x_food = randint(5,pyxel.width - 5)
            y_food = randint(5,pyxel.height - 5)
            print(x_food,y_food)
            self.food.append((x_food,y_food))
            self.numberOfFood += 1
 
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
    
    def drawFood(self):
        for i in self.food:
            pyxel.circ(i[0],i[1],1.5,9)
    def drawSnake(self):
        for i in self.snakeParts:
            pyxel.rect(i[0],i[1],4,4,4)
    def draw(self):
        pyxel.cls(0)
        self.drawSnake()
        self.drawFood()
        
        

App()