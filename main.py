"""All import"""
from classes import Maze
import pygame
from constantes import SIZE
from player import Player

# from item import *

pygame.init()

"""Display windows game"""
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

"""Beginning the game"""
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

    """Move player with keypad and Player class"""
    if event.type == pygame.KEYDOWN:

        if event.key == pygame.K_DOWN:
            homer.move("down")
        if event.key == pygame.K_UP:
            homer.move("up")
        if event.key == pygame.K_LEFT:
            homer.move("left")
        if event.key == pygame.K_RIGHT:
            homer.move("right")


    maze.check_is_item_drop(homer.x,homer.y)
    maze.display(window)
    homer_pos = window.blit(homer.direction, (homer.x, homer.y))
    maze.is_all_item_drop()
    pygame.display.flip()

