import pygame
from pygame.draw import *
from random import randint
from math import sqrt

from colors import *
from ball import Ball

WIDTH_SCREEN = 1000
HEIGHT_SCREEN = 1000

def check_hit(event, ball: Ball):
    """Return true if player hit the ball"""
    x = event.pos[0]
    y = event.pos[1]
    distance = sqrt((x - ball.x)**2 + (y - ball.y)**2)

    if distance < ball.radius:
        return True
    else:
        return False


def new_ball(surface):
    """Get a new ball with random parameters: cordinates, size, color"""
    radius = randint(10, 30)
    color = (randint(0, 255), randint(0, 255), randint(0, 255))
    x = randint(radius, WIDTH_SCREEN - radius)
    y = randint(radius, HEIGHT_SCREEN - radius)
    return Ball(surface, color, (x, y), radius)


def main():
    pygame.init()

    FPS = 30
    screen = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN))
    screen.fill(WHITE)
    pygame.display.update()
    clock = pygame.time.Clock()
    
    finished = False
    ball = ()
    score = 0
    ball = new_ball(screen)
    while not finished:
        clock.tick(FPS)
        ball.move()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if check_hit(event, ball):
                        score += 1
                        print("SCORE: ", score)
                        del ball
                        ball = new_ball(screen)                  
     
        pygame.display.update()
 
    del ball
    pygame.quit()


if __name__ == "__main__":
    main()