"""All import"""
from classes import Maze
import pygame
from constantes import SIZE
from player import Player

# from item import *

pygame.init()

"""Display screen"""
window = pygame.display.set_mode((SIZE, SIZE))
pygame.display.set_caption("Mac_Gyver")
pygame.display.flip()

"""Read file level.txt"""
files = "level"

maze = Maze(files)
maze.generate()
maze.display(window)
homer = Player("src/assets/player.png", maze)
RUNNING = True

"""Beginning of game"""
while RUNNING:
    window.fill((0,0,0))
    continuer_jeu = 1

    while continuer_jeu:

        pygame.time.Clock().tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
                print("croix")
                pygame.quit()
                game = 0

            else:
                continuer_jeu = 0
                game = "src/assets/level.txt"

    """Move player with keypad"""
    if event.type == pygame.KEYDOWN:

        if event.key == pygame.K_DOWN:
            #print("down")
            homer.move("down")
        if event.key == pygame.K_UP:
            #print("up")
            homer.move("up")
        if event.key == pygame.K_LEFT:
            #print("left")
            homer.move("left")
        if event.key == pygame.K_RIGHT:
            #print("right")
            homer.move("right")

    maze.check_is_item_drop(homer.x,homer.y)
    maze.is_all_item_drop(homer.x,homer.y)
    maze.display(window)
    homer_pos = window.blit(homer.direction, (homer.x, homer.y))
    pygame.display.flip()
    
