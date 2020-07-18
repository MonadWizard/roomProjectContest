import pygame
import sys  #sys use to execute our game on consol window
import random  # to generate random food
import time #time is use to define frame/sec

import self as self


class Snake():
    def __init__(self):  # initialize the position and vartical of snake
        self.position = [100,50]  # [100,50] = [cordinate of x position, cordinate of y position]
                        #if we want to move left or right , we need to update x cordinate position ,if we want to move up or down , we need to update y cordinate position
        self.body = [[100,50],[90,50],[80,50]]
        self.direction ="RIGHT"   # define direction in which it moving at a particular time
        self.changeDiractionTo = self.direction  # to change direction

    def changeDirTo(self,dir):
        if dir == "RIGHT" and not self.direction == "LEFT":
            self.direction = "RIGHT"
        if dir == "LEFT" and not self.direction == "RIGHT":
            self.direction = "LEFT"
        if dir == "UP" and not self.direction == "DOWN":
            self.direction = "UP"
        if dir == "DOWN" and not self.direction=="UP":
            self.direction = "DOWN"

    def move(self,foodPos):  # for give food-position , If snake take food it return something unless it return other
        # if we want to move right,then we increse the cordinate of x position
        if self.direction == "RIGHT":
            self.position[0] += 10

        # if we want to move left,then we discrise the cordinate of x position
        if self.direction == "LEFT":
            self.position[0] -= 10

        # if we want to move up,then we decrement the cordinate of x position
        if self.direction == "UP":
            self.position[1] -= 10

        # if we want to move down,then we increse the cordinate of x position
        if self.direction == "DOWN":
            self.position[1] += 10

        """
        we change position now we need to change it's body. so we insert position begnin of the body
        And we need to check if we found food , then size is increse.
        If we don't found food then we need to remove last element of the body
        """

        self.body.insert(0,self.position[:])  # [:] this create new list and insert into body
        if self.position == foodPos:
            return 1
        else:
            self.body.pop()
            return 0


    #check collision = সংঘর্ষের পরীক্ষা
    def checkCollision(self):
        if self.position[0] > 490 or self.position[0]<0:
            return 1
        elif self.position[1] > 490 or self.position[1]<0:
            return 1
        for bodyPart in self.body[1:]:
            if self.position == bodyPart:
                return 1
        return 0
    def getHeadPos(self):
        return self.position

    def getBody(self):
        return self.body



# our screen size is 50 by 50  and element size is 10

class FoodSpawer():
    def __init__(self):  # [define unrandom number for x, y]
        self.position = [random.randrange(1,50)*10,random.randrange(1,50)*10]
        self.isFoodOnScreen = True   # check is food on the screen or not


    # for ree-generate food
    def spawnFood(self):
        if self.isFoodOnScreen == False:
            self.position = [random.randrange(1,50)*10,random.randrange(1,50)*10]
            self.isFoodOnScreen = True
        return self.position       # return new food location


    # define eat food and food isn't on screen
    def setFoodInScreen(self,b):
        self.isFoodOnScreen = b


# define pygame consol to play game
window = pygame.display.set_mode((500,500))
pygame.display.set_caption("Wow Snake")
# define or keep-check frame/sec ,cause by defaultly firster computer can run game very firstly
# we define upper limit of the frame
fps = pygame.time.Clock()

score = 0

snake = Snake()
foodSpawner = FoodSpawer()


def gameOver():
    pygame.quit()
    sys.exit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.changeDirTo('RIGHT')
            if event.key == pygame.K_UP:
                snake.changeDirTo('UP')
            if event.key == pygame.K_LEFT:
                snake.changeDirTo('LEFT')
            if event.key == pygame.K_DOWN:
                snake.changeDirTo('DOWN')

    foodPos = foodSpawner.spawnFood()
    if(snake.move(foodPos)==1):
        score += 1
        foodSpawner.setFoodInScreen(False)

    window.fill(pygame.Color(225,225,225))         # define pygame consol color
    for pos in snake.getBody():
        pygame.draw.rect(window,pygame.Color(0,225,0),pygame.Rect(pos[0],pos[1],10,10))
    # food color
    pygame.draw.rect(window, pygame.Color(225, 0, 0), pygame.Rect(foodPos[0], foodPos[1], 10, 10))

    # check if snake is Collision or crush with something or not
    if(snake.checkCollision() == 1):
        gameOver()

    # score on title par it's self
    pygame.display.set_caption("Careless Snake | Score : " + str(score))

    # we need to reference
    pygame.display.flip()

    # for check fame rate don't excess than 24 middle half first line is it
    fps.tick(10)














