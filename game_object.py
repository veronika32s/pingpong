import pygame

class Board(pygame.Rect):
    def __init__(self,x, y, width, heigth, image, speed):
        super().__init__(x ,y , width, heigth)
        self.IMAGE = image
        self.SPEED = speed
        self.MOVE = {"UP"}