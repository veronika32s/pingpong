import pygame
from data import*
from random import choice, uniform

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



class Ball():
    def __init__(self, x, y,radius,color, image,speed):
        self.X = x
        self.Y = y 
        self.RADIUS = radius
        self.COLOR = color
        self.IMAGE = image
        self.SPEED = speed
        self.ANGLE = choice([-self.SPEED, self.SPEED])
        self.VERTICAL = 0
        self.DIRECTION = True if self.ANGLE < 0 else False

    def move(self, board):
        coff = 0
        if self.Y - self.RADIUS <= 0 or self.Y + self.RADIUS >= setting_win["HEIGHT"]:
           self.VERTICAL *= -1
        elif board.collidepoint(self.X - self.RADIUS, self.Y ) or board.collidepoint(self.X + self.RADIUS,self.Y):
            if board.MOVE["UP"]:
                self.VERTICAL = - uniform(self.SPEED // 2, self.SPEED)
                if self.ANGLE < 0:
                    self.ANGLE = - self.SPEED
                else:
                    self.ANGLE = self.SPEED
                coff = (((self.ANGLE ** 2 + self.VERTICAL ** 2) ** 0.5) / self.SPEED)
                self.ANGLE = self.SPEED / coff
                if  self.DIRECTION:
                    self.ANGLE *= -1 
                self.VERTICAL = self.VERTICAL / coff
            
            elif board.MOVE["DOWN"]:
                self.VERTICAL = uniform(self.SPEED// 2 , self.SPEED)
                if self.ANGLE < 0:
                    self.ANGLE = - self.SPEED
                else:
                    self.ANGLE = self.SPEED
                coff = (((self.ANGLE **2 + self.VERTICAL ** 2) ** 0.5) / self.SPEED)
                self.ANGLE = self.SPEED / coff
                if  self.DIRECTION:
                    self.ANGLE *= -1 
                self.VERTICAL = self.VERTICAL / coff
            self.ANGLE *= -1
            self.DIRECTION = not self.DIRECTION
        
        self.X += self.ANGLE
        self.Y += self.VERTICAL
        #print((self.ANGLE ** 2 + self.VERTICAL ** 2)**0.5 , self.ANGLE , self.VERTICAL,coff)

def win_lose_score(window, ball, board1 , board2,score1 , score2, font):
    window.blit(font.render(f"{score1} : {score2}", True, (128,128,128)), (setting_win["WIDTH"] // 2 - 30 , 10))
    if ball.X - ball.RADIUS  - ball.SPEED < board1.x + board1.width:   
        score2 += 1
        board1.y = start_game ["LEFT_PLAYER"][1]
        board2.y = start_game ["RIGHT_PLAYER"][1]
        ball.X = start_game["BALL"]["START"][0]
        ball.Y = start_game["BALL"]["START"][1]
        ball.ANGLE = start_game["BALL"]["LEFT_PLAYER"]
    elif ball.X + ball.RADIUS  + ball.SPEED > board2.x:
        score1 += 1
        board1.y = start_game ["LEFT_PLAYER"][1]
        board2.y = start_game ["RIGHT_PLAYER"][1]
        ball.X = start_game["BALL"]["START"][0]
        ball.Y = start_game["BALL"]["START"][1]
        ball.ANGLE = start_game["BALL"]["RIGHT_PLAYER"]
    elif score1 == 5:
        ball.SPEED = 0 
        ball.VERTICAL = 0 
        ball.ANGLE = 0 
        board1.SPEED = 0 
        board2.SPEED = 0 
        window.blit(font.render("Лівий гравець переміг"), True ,(128, 128, 128) ,(setting_win["WIDTH"] // 2 - 250 , setting_win["HEIGHT"] // 2 - 25))
        
        
    elif score2 == 5:
        ball.SPEED = 0 
        ball.VERTICAL = 0 
        ball.ANGLE = 0 
        board1.SPEED = 0 
        board2.SPEED = 0 
        window.blit(font.render("Правий гравець переміг"), True ,(128, 128, 128) ,(setting_win["WIDTH"] // 2 - 250 , setting_win["HEIGHT"] // 2 - 25))
        