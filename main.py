import pyxel
from random import randint

WIDTH = 160
HEIGHT = 120
DIRECTION = "N"


class Snake:
    def __init__(self, width, height):
        self.snakeParts = []
        self.snakeMovement = 1
        self.x = width / 2
        self.y = height / 2
        self.snakeParts.append([self.x, self.y, ""])
        self.endPosition = [self.x, self.y, ""]
        self.savePosition = [self.x, self.y, ""]

    def snakeReset(self):
        self.snakeParts = []
        self.x = WIDTH / 2
        self.y = HEIGHT / 2
        self.snakeParts.append([self.x, self.y, ""])
        self.endPosition = [self.x, self.y, ""]
        self.savePosition = [self.x, self.y, ""]
    
    def snakeUpdateMovement(self, direction):
        old_val_x = self.snakeParts[0][0]
        old_val_y = self.snakeParts[0][1]
        old_destiny = self.snakeParts[0][2]
        
        if direction == "N":
            self.snakeParts[0][1] = (self.snakeParts[0][1] - self.snakeMovement) % pyxel.height
            self.snakeParts[0][2] = "N"
        elif direction == "E":
            self.snakeParts[0][0] = (self.snakeParts[0][0] + self.snakeMovement) % pyxel.width
            self.snakeParts[0][2] = "E"
        elif direction == "S":
            self.snakeParts[0][1] = (self.snakeParts[0][1] + self.snakeMovement) % pyxel.height
            self.snakeParts[0][2] = "S"
        else:
            self.snakeParts[0][0] = (self.snakeParts[0][0] - self.snakeMovement) % pyxel.width
            self.snakeParts[0][2] = "W"
        for i in range(1, len(self.snakeParts)):
            save_x = self.snakeParts[i][0]
            save_y = self.snakeParts[i][1]
            save_destination = self.snakeParts[i][2]
            self.snakeParts[i][0] = old_val_x
            self.snakeParts[i][1] = old_val_y
            self.snakeParts[i][2] = old_destiny
            old_val_x = save_x
            old_val_y = save_y
            old_destiny = save_destination
        self.endPosition = [
            self.snakeParts[-1][0], self.snakeParts[-1][1],
            self.snakeParts[-1][2]
        ]
    def createNewPartOfSnake(self):
        if self.endPosition[2] == "N":
            newPartOfSnakeX = self.endPosition[0]
            newPartOfSnakeY = self.endPosition[1] 
            self.snakeParts.append([newPartOfSnakeX, newPartOfSnakeY, "W"])
        elif self.endPosition[2] == "E":
            newPartOfSnakeX = self.endPosition[0] 
            newPartOfSnakeY = self.endPosition[1]
            self.snakeParts.append([newPartOfSnakeX, newPartOfSnakeY, "W"])
        elif self.endPosition[2] == "S":
            newPartOfSnakeX = self.endPosition[0]
            newPartOfSnakeY = self.endPosition[1] 
            self.snakeParts.append([newPartOfSnakeX, newPartOfSnakeY, "W"])
        else:
            newPartOfSnakeX = self.endPosition[0] 
            newPartOfSnakeY = self.endPosition[1]
            self.snakeParts.append([newPartOfSnakeX, newPartOfSnakeY, "W"])
     
    def drawSnake(self):
        counter = 0
        for i in self.snakeParts:
            if counter == 0:
                pyxel.rect(i[0], i[1], 4, 4, 10)
                counter+=1
            else:
                pyxel.rect(i[0], i[1], 4, 4, 4)

    def getSnakePartX(self,index):
        return self.snakeParts[index][0]
    
    def getSnakePartY(self,index):
        return self.snakeParts[index][1]


class Block:
    def __init__(self):
        '''
        Class represent blocks which will be a handicap for a snake
        '''
        self.numberOfBlock = 0
        self.blocks = []
        self.blockArrangement()

    def blockArrangement(self):
        x_block = randint(5,pyxel.width - 10)
        y_block = randint(5,pyxel.height - 10)
        self.blocks.append([x_block,y_block,4,8])
        while len(self.blocks) < 10:
            x_block = randint(5,pyxel.width - 10)
            y_block = randint(5,pyxel.height - 10)
            if [x_block,y_block] in self.blocks:
                continue
            probability = randint(0,10)
            if probability < 5:
                self.blocks.append([x_block,y_block,4,8])
            else:
                self.blocks.append([x_block,y_block,8,4])
    
    def getBlocks(self):
        return self.blocks
    
    def draw(self):
        for i in self.blocks:
            pyxel.rect(i[0],i[1],i[2],i[3],1)

    def resetBlocks(self):
        self.numberOfBlock = 0
        self.blocks = []
        self.blockArrangement()
class App:
    def __init__(self):
        pyxel.init(WIDTH, HEIGHT, quit_key=pyxel.KEY_Q)
        self.direction = DIRECTION
        self.numberOfFood = 0
        self.food = []
        self.snake = Snake(WIDTH, HEIGHT)
        self.block = Block()
        pyxel.run(self.update, self.draw)

    def update(self):
        self.movementCheck()
        self.snake.snakeUpdateMovement(self.direction)
        self.checkCollisionSnakeWithFood()
        self.checkFoodAndUpdate()
        self.checkCollisionWithBlock()

    def collisionStatement(self, foodx, foody, snakeheadx, snakeheady,
                           foodWidht, snakeWidht,foodHeight,snakeHeight):
        if (foodx < snakeheadx + snakeWidht and foodx + foodWidht > snakeheadx
                and foody < snakeheady + snakeHeight
                and foody + foodHeight > snakeheady):
            return True
        return False
    
    def checkCollisionWithBlock(self):
        for i in self.block.getBlocks():
            if self.collisionStatement(i[0],i[1],self.snake.getSnakePartX(0),
                                            self.snake.getSnakePartY(0),i[2],4,i[3],4):
                self.resetGame()
                print("RESET")
                break
    
    def checkCollisionBlockAndFood(self,xfood,yfood,widhtfood,heightfood):
        for i in self.block.getBlocks():
            if self.collisionStatement(i[0],i[1],xfood,yfood,i[2],widhtfood,i[3],heightfood):
                return True
        return False
                
    def resetGame(self):
        self.snake.snakeReset()
        self.block.resetBlocks()

    def checkCollisionSnakeWithFood(self):
        count = 0
        for i in self.food:
            if self.collisionStatement(i[0], i[1], self.snake.getSnakePartX(0),
                                       self.snake.getSnakePartY(0), 1.5, 4,1.5,4):
                del self.food[count]
                self.snake.createNewPartOfSnake()
                self.numberOfFood -= 1
                break
            count += 1

    def checkFoodAndUpdate(self):
        if self.numberOfFood == 0 or self.numberOfFood < 5:
            x_food = randint(5, pyxel.width - 5)
            y_food = randint(5, pyxel.height - 5)
            while self.checkCollisionBlockAndFood(x_food,y_food,1.5,1.5) == True:
                x_food = randint(5, pyxel.width - 5)
                y_food = randint(5, pyxel.height - 5)
            print(x_food, y_food)
            self.food.append((x_food, y_food))
            self.numberOfFood += 1

    def movementCheck(self):
        if pyxel.btnp(pyxel.KEY_LEFT):
            self.direction = "W"
        if pyxel.btnp(pyxel.KEY_RIGHT):
            self.direction = "E"
        if pyxel.btnp(pyxel.KEY_UP):
            self.direction = "N"
        if pyxel.btnp(pyxel.KEY_DOWN):
            self.direction = "S"

    def drawFood(self):
        for i in self.food:
            pyxel.circ(i[0], i[1], 1.5, 9)

    def draw(self):
        pyxel.cls(0)
        self.snake.drawSnake()
        self.drawFood()
        self.block.draw()


App()