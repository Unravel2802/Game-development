import pygame
import random
speed = 20
size = 20

class Player():
    def __init__(self, xpos, ypos, color):
        self.xpos = xpos
        self.ypos = ypos
        self.color = color
        self.rect = (self.xpos, self.ypos)
        self.xvel = 0
        self.yvel = 0
        self.length = 1
        self.parts = []
        self.head = []
        self.head.append(self.xpos)
        self.head.append(self.ypos)
        self.parts.append(self.head)
        self.food_pos = []


    def draw(self, win):
        for part in self.parts:
            pygame.draw.rect(win, self.color, (part[0], part[1], size, size))
    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.xvel != speed:
            self.xvel = -1 * speed
            self.yvel = 0

        if keys[pygame.K_RIGHT] and self.xvel != -1 * speed:
            self.xvel = speed
            self.yvel = 0

        if keys[pygame.K_UP] and self.yvel != speed:
            self.xvel = 0
            self.yvel = -1 * speed

        if keys[pygame.K_DOWN] and self.yvel != -1 * speed:
            self.xvel = 0
            self.yvel = speed

        if keys[pygame.K_ESCAPE]:
            exit()

        self.xpos += self.xvel
        self.ypos += self.yvel
        if len(self.parts)>0:
            self.parts.pop(0)

        self.update()

    def eat(self):
        self.length += 1

    def Food(self, win):

        while not self.food_pos:
            x = round(random.randrange(0, 800 - 2*size) / 20.0) * 20.0
            y = round(random.randrange(0, 800 - 2*size) / 20.0) * 20.0
            if not [x, y] in self.parts:
                self.food_pos = [x, y]
        pygame.draw.rect(win, (255, 0, 0), (self.food_pos[0], self.food_pos[1], 20, 20))

        if [self.xpos,self.ypos] == self.food_pos:
            self.food_pos = []
            self.parts.insert(0, self.parts[0])
    #def drawFood(self, win):
        #pygame.draw.rect(win, (255, 0, 0), (self.food_pos[0], self.food_pos[1], 20, 20))

    #def drawFood(self, win):

    def check_tail_collision(self):
        head = self.parts[-1]
        has_eaten_tail = False

        for i in range(len(self.parts) - 1):
            segment = self.parts[i]
            if head[0] == segment[0] and head[1] == segment[1]:
                has_eaten_tail = True

        return has_eaten_tail

    def check_border_collision(self, w, h):
        end = False
        if self.xpos >= w or self.xpos < 0 or self.ypos >= h or self.ypos < 0:
            end = True
        return end

    def check_player_collision(self, p):
        head = self.parts[-1]
        end = False

        for i in range(len(p.getParts())-1):
            segment = p.parts[i]
            if head[0] == segment[0] and head[1] == segment[1]:
                end = True
        return end

    def printLose(self):
        #if self.check_player_collision(p):
        #print("Oops, you got into the other player, you lose!")
        print("You lose!")
        exit()

    def printWin(self):
        #if self.check_player_collision(p):
        #print("Oops, the other player got into you, you win!")
        print("You win!")
        exit()

    def getParts(self):
        return self.parts

    def getLen(self):
        return len(self.parts)

    def getHead(self):
        return self.parts[-1]

    def update(self):
        self.rect = (self.xpos, self.ypos)
        self.parts.append(self.rect)
