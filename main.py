import pygame 

pygame.init()

window = pygame.display.set_mode((800,500))
pygame.display.set_caption("ping-pong")

def run():
    game = True 

    while game:

        for event in pygame.get():
            if event.type == pygame.QUIT:
                game = False

run()