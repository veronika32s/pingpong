import pygame

class Board(pygame.Rect):
    def __init__(self,x, y, width, heigth, image, speed):
        super().__init__(x ,y , width, heigth)
        self.IMAGE = image
        self.SPEED = speed
        self.MOVE = {"UP":False,"DOWN":False}

    def move(self):
        if self.MOVE["UP"] and self.y > 0 :
            self.y -= self.SPEED
        elif self.MOVE["DOWN"] and self.y < 400:
            self.y += self.SPEED
        #print(1)