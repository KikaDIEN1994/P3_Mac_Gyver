from constantes import SPRITE_NUMBER, SPRITE_SIZE
import pygame
from classes import Maze


class Player:
    """init player position and picture"""
    def __init__(self, player, maze):
        self.player = pygame.image.load("src/assets/img/player.png").convert_alpha()
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0
        self.direction = self.player
        self.maze = maze

    """This method is use for move player in each direction
        and we add 1 condition for collision 
    """
    def move(self, direction):

        if direction == "right":
            if self.case_x < (SPRITE_NUMBER - 1):
                if self.maze.structure[self.case_y][self.case_x + 1] == "G":
                    #print("gagner")  # change all
                    #pygame.quit()
                    pass
                if self.maze.structure[self.case_y][self.case_x + 1] != "#":
                    self.case_x += 1
                    self.x = self.case_x * SPRITE_SIZE
            self.player

        if direction == "left":
            if self.case_x > 0:
                if self.maze.structure[self.case_y][self.case_x - 1] != "#":
                    self.case_x -= 1
                    self.x = self.case_x * SPRITE_SIZE
            self.player

        if direction == "up":
            if self.case_y > 0:
                if self.maze.structure[self.case_y - 1][self.case_x] != "#":
                    self.case_y -= 1
                    self.y = self.case_y * SPRITE_SIZE
            self.player

        if direction == "down":
            if self.case_y < (SPRITE_SIZE - 1):
                if self.maze.structure[self.case_y + 1][self.case_x] != "#":
                    self.case_y += 1
                    self.y = self.case_y * SPRITE_SIZE
            self.player
