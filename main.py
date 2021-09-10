"""All import"""
from classes import Maze
import pygame
from constantes import SIZE
from player import Player


pygame.init()

font = pygame.font.Font(None, 72)
WIN = font.render("YOU WIN", 1, (255, 255, 255))
LOOSE = font.render("YOU LOOSE", 1, (255, 255, 255))

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
    window.fill((0, 0, 0))

    pygame.time.Clock().tick(15)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
            print("croix")
            pygame.quit()
            exit()

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

    maze.check_is_item_drop(homer.x, homer.y)
    maze.display(window)
    homer_pos = window.blit(homer.direction, (homer.x, homer.y))

    if maze.is_finished(homer.x, homer.y):
        if maze.is_all_item_drop():
            window.blit(WIN, (370, 400))
        else:
            window.blit(LOOSE, (370, 400))
        pygame.display.flip()
        pygame.time.delay(2000)
        pygame.quit()
        exit()

    pygame.display.flip()
