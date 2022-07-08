from pygame.draw import *
from random import randint
from random import uniform
from math import sqrt

from colors import *


class Ball:
    def __init__(self, surface, color = RED, cords = (0, 0), radius = 10, max_speed = 10.0) -> None:
        self.color = color
        self.x = cords[0]
        self.y = cords[1]
        self.radius = radius
        self.surface = surface
        self.__print()

        self.__speed = uniform(1, max_speed)
        self.__mov_x = uniform(-self.__speed, self.__speed)
        self.__mov_y = sqrt(self.__speed**2 - self.__mov_x**2)
        if randint(0, 1):
            self.__mov_y = -self.__mov_y

    def __str__(self) -> str:
        return f"Color: {self.color}\nCords: ({self.x}, {self.y})\nRadius: {self.radius}"

    def __del__(self) -> None:
        self.__clear()

    def __clear(self) -> None:
        """Clear previous ball location"""
        circle(self.surface, WHITE, (self.x, self.y), self.radius)
    
    def __print(self) -> None:
        """Print ball in new location"""
        circle(self.surface, self.color, (self.x, self.y), self.radius) 

    def get_speed(self) -> float:
        return self.__speed

    #def change_speed()

    def move(self):
        """Move ball in new location with check with check the borders screen"""
        self.__clear()
        right_x = self.x + self.radius + self.__mov_x
        if right_x > self.surface.get_width():
            self.__mov_y = uniform(self.__speed, -self.__speed)
            self.__mov_x = -sqrt(self.__speed**2 - (self.__mov_y**2))
            
        left_x = self.x - self.radius + self.__mov_x
        if left_x < 0:
            self.__mov_y = uniform(self.__speed, -self.__speed)
            self.__mov_x = sqrt(self.__speed**2 - (self.__mov_y**2))

        right_y = self.y + self.radius + self.__mov_y
        if right_y > self.surface.get_height():
            self.__mov_x = uniform(self.__speed, -self.__speed)
            self.__mov_y = -sqrt(self.__speed**2 - (self.__mov_x**2))

        left_y = self.y - self.radius + self.__mov_y
        if left_y < 0:
            self.__mov_x = uniform(self.__speed, -self.__speed)
            self.__mov_y = sqrt(self.__speed**2 - (self.__mov_x**2))

        self.x += self.__mov_x
        self.y += self.__mov_y
        self.__print()