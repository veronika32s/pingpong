import pygame
from data import*
from random import choice, uniform
import time

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
        self.SCORE1 = 0 
        self.SCORE2 = 0 
        self.WIN = True

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
        elif True:
            pass
        self.X += self.ANGLE
        self.Y += self.VERTICAL
        #print((self.ANGLE ** 2 + self.VERTICAL ** 2)**0.5 , self.ANGLE , self.VERTICAL,coff)

def win_lose_score(window, ball, board1 , board2 , font):
    window.blit(font.render(f"{ball.SCORE1} : {ball.SCORE2 }", True, (128,128,128)), (setting_win["WIDTH"] // 2 - 30 , 10))
    if ball.X - ball.RADIUS   < board1.x + board1.width - ball.RADIUS:   
        ball.SCORE2 += 1
        board1.y = start_game ["LEFT_PLAYER"][1]
        board2.y = start_game ["RIGHT_PLAYER"][1]
        ball.X = start_game["BALL"]["START"][0]
        ball.Y = start_game["BALL"]["START"][1]
        ball.ANGLE = start_game["BALL"]["LEFT_PLAYER"]
        ball.VERTICAL = 0 
        time.sleep(2)

    elif ball.X + ball.RADIUS   > board2.x + ball.RADIUS:
        ball.SCORE1 += 1
        board1.y = start_game ["LEFT_PLAYER"][1]
        board2.y = start_game ["RIGHT_PLAYER"][1]
        ball.X = start_game["BALL"]["START"][0]
        ball.Y = start_game["BALL"]["START"][1]
        ball.ANGLE = start_game["BALL"]["RIGHT_PLAYER"]
        ball.VERTICAL = 0 
        time.sleep(2)

    elif ball.SCORE1 == 1:
        if ball.WIN :
            stop_game(ball, board1, board2) 
            ball.WIN = False
        pygame.draw.rect(window,(64, 31, 251),button_list[0])
        pygame.draw.rect(window,(64, 31, 251),button_list[1])
        window.blit(button_list[2],(setting_win["WIDTH"] // 2 - setting_rect["WIDTH"] // 2 + 75,
                                    setting_win["HEIGHT"] // 2 - setting_rect["HEIGHT"] - 5))
        window.blit(button_list[3],(setting_win["WIDTH"] // 2 - setting_rect["WIDTH"] // 2 + 20,
                                    setting_win["HEIGHT"] // 2 + 35))
        window.blit(font.render("Лівий гравець переміг", True ,(128, 128, 128)) ,(setting_win["WIDTH"] // 2 - 250 , setting_win["HEIGHT"] // 2 - 25))
        pygame.display.flip()
        
    elif ball.SCORE2  == 1: 
        if ball.WIN:
            stop_game(ball, board1, board2)
            ball.WIN = False
        pygame.draw.rect(window,(64, 31, 251),button_list[0])
        pygame.draw.rect(window,(64, 31, 251),button_list[1])
        window.blit(button_list[2],(setting_win["WIDTH"] // 2 - setting_rect["WIDTH"] // 2 + 75,
                                    setting_win["HEIGHT"] // 2 - setting_rect["HEIGHT"] - 5))
        window.blit(button_list[3],(setting_win["WIDTH"] // 2 - setting_rect["WIDTH"] // 2 + 20,
                                    setting_win["HEIGHT"] // 2 + 35))
        window.blit(font.render("Правий гравець переміг", True ,(128, 128, 128)) ,(setting_win["WIDTH"] // 2 - 250 , setting_win["HEIGHT"] // 2 - 25))
        pygame.display.flip()

def stop_game(ball,board1, board2):
    ball.SPEED = 0 
    ball.VERTICAL = 0 
    ball.ANGLE = 0 
    board1.SPEED = 0 
    board2.SPEED = 0 
    font = pygame.font.Font(None,50)
    button_list.append(pygame.Rect(setting_win["WIDTH"] // 2 - setting_rect["WIDTH"] // 2 , 
                                   setting_win["HEIGHT"] // 2 - setting_rect["HEIGHT"] - 25,
                                    setting_rect["WIDTH"] ,
                                     setting_rect["HEIGHT"] ))
    button_list.append(pygame.Rect(setting_win["WIDTH"] // 2 - setting_rect["WIDTH"] // 2 , 
                                    setting_win["HEIGHT"] // 2 + 15,
                                    setting_rect["WIDTH"] ,
                                    setting_rect["HEIGHT"] ))
    button_list.append(font.render("Нова гра" , True, (255,255,255)))
    button_list.append(font.render("Завершити гру" , True, (255,255,255)))

def restart_game(ball, board1, board2):
    ball.SPEED = setting_ball["SPEED"]
    board1.SPEED = setting_board["SPEED"]
    board2.SPEED = setting_board["SPEED"]
    ball.ANGLE = choice([-ball.SPEED, ball.SPEED])
    ball.DIRECTION = True if ball.ANGLE < 0 else False
    ball.WIN = True
    ball.SCORE1 = 0
    ball.SCORE2 = 0
