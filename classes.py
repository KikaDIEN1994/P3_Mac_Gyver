import pygame
import random
from constantes import WALL, FLOOR, GUARDIAN
from constantes import ITEM_0, ITEM_1, ITEM_2, SPRITE_SIZE
from item import Item

"""This class read and generate the labyrinth"""


class Maze:
    """Init file level.txt and create an empty list items"""

    def __init__(self, file):
        self.file = "src/assets/level.txt"
        self.structure = 0
        self.items = []
        self.guardian_x = None
        self.guardian_y = None

    """Read file level.txt"""

    def generate(self):
        # read each line of level.txt
        with open(self.file, "r") as file:
            self.structure = [list(line) for line in file.read().split("\n")]
            # items_pos_available[] is a list composed of " "(floor) for drop items
            items_pos_available = [
                (i, j)
                for j, line in enumerate(self.structure)
                for i, val in enumerate(line)
                if val == " "
            ]
            # We use 3 times items_pos_available.pop() for not having same position
            random.shuffle(items_pos_available)
            i, j = items_pos_available.pop()
            self.items.append(Item(i, j, pygame.image.load(ITEM_0).convert()))
            i, j = items_pos_available.pop()
            self.items.append(Item(i, j, pygame.image.load(ITEM_1).convert()))
            i, j = items_pos_available.pop()
            self.items.append(Item(i, j, pygame.image.load(ITEM_2).convert()))

    def display(self, window):
        # From level.txt convert all fix character to image (WALL,FLOOR,GUARDIAN)
        WALLS = pygame.image.load(WALL).convert()
        FLOORS = pygame.image.load(FLOOR).convert_alpha()
        GUARDIANS = pygame.image.load(GUARDIAN).convert()

        num_line = 0
        for line in self.structure:
            num_case = 0
            for sprite in line:
                x = num_case * SPRITE_SIZE
                y = num_line * SPRITE_SIZE
                if sprite == "#":
                    window.blit(WALLS, (x, y))
                elif sprite == " ":
                    window.blit(FLOORS, (x, y))
                elif sprite == "G":
                    window.blit(GUARDIANS, (x, y))
                    self.guardian_x = x
                    self.guardian_y = y
                num_case += 1
            num_line += 1
        for item in self.items:
            if not item.is_item_drop():
                window.blit(item.image, (item.x * SPRITE_SIZE, item.y * SPRITE_SIZE))

    # Methode that check if item is drop and remove item
    def check_is_item_drop(self, homer_x, homer_y):
        for item in self.items:
            if item.x * SPRITE_SIZE == homer_x and item.y * SPRITE_SIZE == homer_y:
                item.drop_item()

    # Counter of item if 3 item drop homer win if not lose
    def is_all_item_drop(self):
        for item in self.items:
            if not item.is_item_drop():
                # print("perdu")
                return False
        return True
        # print("3 objets")

    def is_finished(self, homer_x, homer_y):
        if self.guardian_x == homer_x and self.guardian_y == homer_y:
            return True
        return False
