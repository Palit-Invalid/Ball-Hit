import pygame
from pygame.draw import *
from random import randint
from math import sqrt
import os

from colors import *
from ball import Ball
from playerlist import PlayerList

def clear_screen():
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')

def check_hit(event, balls: list):
    """Return true if player hit the ball"""
    x = event.pos[0]
    y = event.pos[1]
    for index, ball in enumerate(balls):
        distance = sqrt((x - ball.x)**2 + (y - ball.y)**2)
        if distance < ball.radius:
            del balls[index]

def new_ball(surface, width, height):
    """Get a new ball with random parameters: cordinates, size, color"""
    radius = randint(10, 30)
    color = (randint(0, 255), randint(0, 255), randint(0, 255))
    x = randint(radius, width - radius)
    y = randint(radius, height - radius)
    return Ball(surface, color, (x, y), radius)

def move_balls(balls: list):
    for ball in balls:
        ball.move()

def start_game(width=400, height=400, num_balls=3, fps=30) -> float:
    
    # Setup game
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    screen.fill(WHITE)
    clock = pygame.time.Clock()
    balls = [new_ball(screen, width, height) for i in range(num_balls)]
    
    # Game cycle
    run = True
    while run:
        clock.tick(fps)
        move_balls(balls)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    check_hit(event, balls) 
                    if len(balls) < 1:
                        run = False                
     
        pygame.display.update()
    
    del balls
    time = pygame.time.get_ticks()/1000
    pygame.quit()
    return time
    
def main():
    records = PlayerList("records")

    width_screen = 500
    height_screen = 500
    num_balls = 10
    fps = 60

    run = True
    while run:
        clear_screen()
        answer = int(input("1. New game\n2. Settings game\n3. Table records\n4. Exit\n"))
        if answer == 1:
            playername = input("Enter your name: ")
            time = start_game(width_screen, height_screen, num_balls, fps)
            records.update_record(playername, time)
        elif answer == 2:
            width_screen = int(input("Current width screen {0}\nEnter new value -> ".format(width_screen)))
            height_screen = int(input("Current height screen {0}\nEnter new value -> ".format(height_screen)))
            num_balls = int(input("Current number of balls {0}\nEnter new value -> ".format(num_balls)))
            fps = int(input("Current FPS {0}\nEnter new value -> ".format(fps)))
        elif answer == 3:
            records.print_all()
            input()
        elif answer == 4:
            run = False


if __name__ == "__main__":
    main()